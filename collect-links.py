#!/usr/bin/env python3

import sys
import requests

# Allows different tags to pull urls from

if len(sys.argv) <= 1:
    sys.exit("No tags selected. Tags: core, mtgame, mtmods, contentdb")

urls = []

if "core" in sys.argv:
    urls.append("https://github.com/minetest/minetest/archive/master.zip")
    print("Added minetest/minetest")

if "mtgame" in sys.argv:
    urls.append("https://github.com/minetest/minetest_game/archive/master.zip")
    print("Added minetest/minetest_game")

if "mtmods" in sys.argv:
    r = requests.get("https://api.github.com/users/minetest-mods/repos")
    if r.status_code != 200:
        sys.exit("Request failed!")

    for project in r.json():
        urls.append(project["html_url"] + "/archive/master.zip")
        print("Added: " + project["full_name"])

if "contentdb" in sys.argv:
    r = requests.get("https://content.minetest.net/api/packages/")
    if r.status_code != 200:
        sys.exit("Request failed!")

    for project in r.json():
        if project["type"] != "txp":
            urls.append("https://content.minetest.net/packages/" + project["author"] + "/" + project["name"] + "/download/")
            print("Added: " + project["title"])

file = open("sources.txt", "w")
file.write("\n".join(urls) + "\n")
print("Wrote " + str(len(urls)) + " links to file.")
