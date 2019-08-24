Static Remote Media Server
==========================

A static Minetest Media Server done simple.

### Why static?
For all other remote media services you need a paid root server.  
But you can everywhere get a simple static webserver where you just need to upload the medias.  
Sadly github pages don't work as they return 405 Not Allowed if you send post data.
There are enough other ones.

### Installation
Just copy your media cache file after you joined the servers you want to have the medias from.  
Next you execute the make_index_mth.py file `python make_index_mth.py`  
Last you just copy the new media file which now includes the index.mth to your webserver  
Then you only need to set in your serverconfig the link to the media_server  
`http://yourdomain.com/media/`

Only Code Licensed under:
MIT
