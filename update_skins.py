import sys, requests, hashlib, base64

print("Downloading skins from minetest.fensta.bplaced.net ...")
r = requests.get('http://minetest.fensta.bplaced.net/api/v2/get.json.php?getlist&page=1&per_page=9999999999')

if r.status_code != 200:
    sys.exit("Request failed!")

data = r.json()
count = 0

print("Writing to file and downloading previews ...")
for json in data["skins"]:
    raw_data = base64.b64decode(json["img"])
    sha1 = hashlib.sha1(raw_data)
    file = open("m/" + sha1.hexdigest(), "wb")
    file.write(bytearray(raw_data))
    file.close()
    id = str(json["id"])
    r2 = requests.get('http://minetest.fensta.bplaced.net/skins/1/' + id + ".png")
    if r.status_code == 200:
        data2 = r2.content
        sha12 = hashlib.sha1(data2)
        file = open("m/" + sha12.hexdigest(), "wb")
        file.write(bytearray(data2))
        file.close()
        # Read meta datas
        name = str(json["name"])
        author = str(json["author"])
        license = str(json["license"])
        print("Added #%s Name: %s Author: %s License: %s" % (id, name, author, license))

    else:
        print("Fetching of preview of skin " + id + "failed!")

    count += 1

print("Fetched " + str(count) + " skins!")
