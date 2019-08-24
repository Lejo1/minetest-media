#Use this script to join all servers on the serverlist automaticly to fetch their media
#Use break-mt to terminate in 0.4 and this mod will also crash 5.0 :)
#use python3.6
import sys, subprocess, requests
player_name = "mediafetcher"
password = "verysecret"
path_to_new_mt = "/home/user/minetest/bin/minetest"
path_to_old_mt = "/home/user/Desktop/Minetest-0.4.16.AppImage"

def do_mt(address, port, path):
    subprocess.run(path + " --go --address " + address + " --port " +
    port + " --name " + player_name + " --password " + password, shell=True)

print("Loading from serverlist...")
r = requests.get("http://servers.minetest.net/list")

if r.status_code != 200:
    sys.exit("Request failed!")

data = r.json()
for json in data["list"]:
    address = json["address"]
    port = str(json["port"])
    name = json["name"]
    leng = len(name) + 11
    print("#"*leng)
    print("#Joining: " + json["name"] + "#")
    print("#"*leng)
    if json["proto_min"] > 32:
        do_mt(address, port, path_to_new_mt)
    else:
        do_mt(address, port, path_to_old_mt)

print("Done.")
