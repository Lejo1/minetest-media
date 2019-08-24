import sys, requests, hashlib

print "Downloading skins from minetest.fensta.bplaced.net ..."
r = requests.get('http://minetest.fensta.bplaced.net/api/v2/get.json.php?getlist&page=1&per_page=9999999999')

if r.status_code != 200:
    sys.exit("Request failed!")

data = r.json()
count = 0

print "Writing to file and downloading previews ..."
for json in data["skins"]:
    raw_data = json["img"].decode('base64')
    sha1 = hashlib.sha1(raw_data)
    file = open("media/" + sha1.hexdigest(), "w")
    file.write(raw_data)
    file.close()
    id = str(json["id"])
    r2 = requests.get('http://minetest.fensta.bplaced.net/skins/1/' + id + ".png")
    if r.status_code == 200:
        data2 = r2.content
        sha12 = hashlib.sha1(data2)
        file = open("media/" + sha12.hexdigest(), "w")
        file.write(data2)
        file.close()

    else:
        print "Fetching of preview of skin " + id + "failed!"

    count += 1

print "Fetched " + str(count) + " skins!"
