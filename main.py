import instagram
import asyncio
import aiohttp
import pathlib
import argparse
import yarl 

from datetime import date

# hacky lazy solution for right now
def fetch_all(func, *args):
    responses = []
    next_id = None
    counter = 0

    while True:
        # while true loops are scary and this number came to me in a dream
        # should never reach this unless someone has more than ~150k posts
        # saved, which is an external problem.
        if counter == 10000:
            break
        
        data, next_id = func(*args, next_id=next_id)
        responses.extend(data)
        counter += 1

        if not next_id:
            break

    return responses


def list_collections(collections):
    for _, c in enumerate(collections):
        if c.type == "ALL_MEDIA_AUTO_COLLECTION":
            print(f" - {c.name:<12} {c.size:>7} posts{'':<5} (-)")
        else:
            print(f" - {c.name:<12} {c.size:>7} posts{'':<5} ({c.id})")
     

async def download_collection(
        session: instagram.Session, c: instagram.Collection, output: pathlib.Path, resume=None):
    # would it be insane to use fetch_all here?
    print(f"[+] Downloading collection {c.name} ({c.id})")

    more_available = True
    index = 0

    if resume is not None:
        rid, index, next_id = resume.split(":")
        index = int(index)
        
        if rid != c.id:
            print(f"[!] next_id does not correspond to this collection ({c.id})")
            return
        
        print(f"[!] Starting from next_id={next_id}")

    while more_available:
        posts, next_id = instagram.fetch_collection_posts(session, c, next_id)

        if not next_id:
            more_available = False

        _id_cache_write(f"{c.id}:{index}:{next_id}")

        tasks = []
        for p in posts:
            targets = list(zip(p.get_filenames(), p.get_urls()))
            for t in targets:
                coro = download_file(t[1], t[0], index, verbose=False, path=output)
                tasks.append(asyncio.create_task(coro))

            index += 1
            
        await asyncio.gather(*tasks)
        print(f"  - Fetched {len(posts)} posts. Progress ({index}/{c.size})")
        
    print("[+] Done.")


async def download_file(url, filename, index=None, verbose=False, path=None):
    url = yarl.URL(url, encoded=True)

    if index is not None:
        filename = f"{index}_{filename}"

    if path is not None:
        path = pathlib.Path(path)
    else:
        path = pathlib.Path(".")

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(path / filename, 'wb+') as file:
                chunk = await response.read()
                file.write(chunk)

            if verbose:
                print(f"[+] Finished downloading {path / filename}")


def _id_cache_write(next_id: str):
    with open(".id_cache", "w+") as cache:
        cache.write(next_id)


async def main():
    collections = fetch_all(instagram.fetch_collections, session)

    if not args.collections:
        # download everything
        # index 0 should be "All Posts", but if you want to be absolutely certain
        # iterate through the collections until id == "ALL_MEDIA_AUTO_COLLECTION"
        for c in collections:
            if c.id == "ALL_MEDIA_AUTO_COLLECTION":
                await download_collection(session, c, output_dir, resume=args.resume)
                break

    else:
        targets = [c for c in collections if c.id in args.collections]
        if not targets:
            print("No collection(s) found matching the supplied id(s)")

        for target in targets:
            await download_collection(session, target, output_dir, resume=args.resume)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-l", "--login", nargs=2, 
                    help="attempt to login with \"username password\"")
    
    parser.add_argument("-s", "--session", help="set `sessionid` cookie")

    parser.add_argument("-o", "--output-dir", default="./saved-posts/",
                    help="directory to save posts")
    
    parser.add_argument("-c", "--list-collections", action="store_true",
                    help="list all collections belonging to an account")
    
    parser.add_argument("-d", nargs="*", dest="collections",
                    help="ids of collections to download from " \
                    "(if no ids are provided the script will attempt to download posts from all collections)")
    
    parser.add_argument("-r", "--resume", help="Begin downloading from a collection at the given next_id")

    args = parser.parse_args()

    if args.login:
        session = instagram.Session(username=args.login[0], password=args.login[1])

    elif args.session:
        session = instagram.Session(token=args.session)

    else:
        parser.print_help()
        exit()

    output_dir = pathlib.Path(args.output_dir) / str(date.today())
    output_dir.mkdir(exist_ok=True, parents=True)

    if args.list_collections:
        print("[+] Collection(s) owned by current account\n")
        collections = fetch_all(instagram.fetch_collections, session)
        list_collections(collections)

    elif args.collections is not None:
        asyncio.run(main())

    else:
        parser.print_help()
        exit()