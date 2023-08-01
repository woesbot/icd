# Instagram Collection Downloader

I wrote this script because I wanted to download my saved posts and the third-party APIs 
I found on Github didn't work for me.

Just a warning, this script really is not focused on interacting with the API in a way that 
appears authentic. So if you care about your account and decide to use this, understand the 
risk.

Files are downloaded into a folder called "saved-posts" created in whatever directory the 
script is invocated from. 
The script also generates a file named ".id_cache" in this directory to store the current
`next_id` of request batch. This is primarily used to quickly resume downloading from a fixed
point if anything goes awry with the with a batch. 

# TODO (when I feel like it)

- Refactor code
- Add download filters

# Reminders

The only cookies you need to be able to receive data back from the API are: 
``session_id``. Other required cookies should be set automatically when interacting
with the web server.

When fetching posts the API returns a list of media confined to the following [structure](docs/media.md).
Since this project is just about getting saved posts, the most important fields are ``image_versions2`` candidates,
and fields that can provide useful metadata, such as `pk`, `id`, `epoch`, `username`, and `code`.
