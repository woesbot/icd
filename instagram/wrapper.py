import requests
import time

from instagram import parser

IG_API_BASE = "https://www.instagram.com/api/v1"
BASE_HEADERS = {"X-IG-APP-ID": "936619743392459"}
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"]


def _error(code, message):
    print(f'[!] {message}')
    exit(code)


def _res_error(response, message):
    # TODO: Change this maybe
    print(f'[!] ({response.status_code}). {message}')
    print(f'{response.content}\n')
    exit()


def _json_res(response) -> bool:
    return 'application/json' in response.headers.get('Content-Type', '')


# Instagram API session
class Session:
    def __init__(self, username=None, password=None, token=None, agent=None):
        self.uid:   str = None
        self.sid:   str = None
        self.agent: str = agent if agent else USER_AGENTS[0]

        self.__internal_session = None

        if username and password:
            self.login(username, password)
        else:
            self.login_with_token(token)

    def login_with_token(self, token: str):
        self.sid = token
        self.uid = token.split("%3A")[0] # "%3A" -> ":"

        self.__internal_session = self.__new_session()

    def login(self, username: str, password: str):
        url = f"{IG_API_BASE}/web/accounts/login/ajax"

        session = self.__new_session()
        data = {
            "optIntoOneTap": False,
            "queryParams": "{}",
            "trustedDeviceRecords": "{}",
            "username": username,
            "enc_password": f"#PWD_INSTAGRAM1BROWSER:0:{int(time.time())}:{password}"
        }

        res = session.post(url, data)

        if res.status == 200 and _json_res(res):
            data = res.json()
            if not data.get("authenticated") or not data.get("user"):
                _error(-1, "Failed to authenticate with the given username and password")

            self.sid = res.cookies.get("sessionid")
            self.uid = data.get("userId")
            self.__internal_session = session
        else:
            _res_error(res, "Error attempting to login")

    def get(self, *args, **kwargs):
        # print(self.__internal_session.cookies.items(s))
        return self.__internal_session.get(*args, **kwargs)

    def post(self, *args, **kwargs):
        #print(self.__internal_session.cookies.items())
        return self.__internal_session.post(*args, **kwargs)

    def __cookies(self):
        return {"ds_user_id": self.uid, "sessionid": self.sid}
    
    def __new_session(self):
        session = requests.Session()
        session.headers.update(BASE_HEADERS)

        # my hatred for python is ever growing 
        for k, v in self.__cookies().items():
            session.cookies.set(k, str(v), domain=".instagram.com")

        # build off of base
        session.headers.update({"User-Agent": USER_AGENTS[0]})
        return session


class Collection:
    def __init__(self, values: dict):
        self.id = None
        self.name = None
        self.type = None
        self.size = None

        self.__url = None

        self._from_dict(values)

    def url(self):
        return self.__url

    def _from_dict(self, values):
        self.id = values.get("collection_id")
        self.name = values.get("collection_name")
        self.type = values.get("collection_type")
        self.size = values.get("collection_media_count")

        if self.type == "ALL_MEDIA_AUTO_COLLECTION":
            self.__url = f"{IG_API_BASE}/feed/saved/posts/"
        else:
            self.__url = f"{IG_API_BASE}/feed/collection/{self.id}/posts/"

        return self

    def __str__(self):
        return f"Collection(id={self.id}, name=\"{self.name}\", size={self.size})"
    

# my hatred of python is waning
def fetch_collections(session: Session, next_id: str = None) -> tuple[list[Collection], str]:
    endpoint = f"{IG_API_BASE}/collections/list/"
    
    params = {
        'collection_types': '["ALL_MEDIA_AUTO_COLLECTION","MEDIA","AUDIO_AUTO_COLLECTION"]',
        'include_public_only': 0,
        'get_cover_media_lists': True,
        'max_id': next_id
    }
    
    res = session.get(endpoint, params=params)

    if res.status_code != 200 or not _json_res(res):
        _res_error(res, "Error fetching saved collections.")
    
    collections = []
    data = res.json()

    for c in data.get("items", []):
        collections.append(Collection(c))

    return (collections, data.get("next_max_id"))


def fetch_collection_posts(session, collection: Collection, next_id: str = None):
    endpoint = collection.url()
    params = {
        "max_id": next_id
    }

    res = session.get(endpoint, params=params)
    if res.status_code != 200 or not _json_res(res):
        _res_error(res, f"Error fetching posts for collection.id:{collection.id}")

    posts = []
    data = res.json()

    for post in data.get("items", []):
        media = post.get('media', {})
        posts.append(parser.parse_media(media))

    return (posts, data.get("next_max_id"))
