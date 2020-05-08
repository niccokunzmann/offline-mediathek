#!/usr/bin/python3

import os
import json

HERE = os.path.dirname(__file__) or "."
CONTENT = os.path.join(HERE, "content")
INDEX = os.path.join(HERE, "index.js")

add = {}

def add_picture(entry, path):
    entry["thumb"] = path
add[".jpg"] = add_picture

def add_video(entry, path):
    entry["video"] = path
add[".mp4"] = add_video

def add_description(entry, path):
    with open(path) as file:
        entry["description"] = file.read()
add[".description"] = add_description

def add_nothing(entry, path):
    pass
add[".sh"] = add_nothing

def add_default(entry, path):
    print("skip", path)

index = {}
for path, dirnames, fnames in os.walk(CONTENT):
    for fname in fnames:
        fid, ext = os.path.splitext(fname)
        index.setdefault(fid, {})
        entry = index[fid]
        entry_path = os.path.join(path, fname)
        func = add.get(ext, add_default)
        func(entry, entry_path)
        print(".", end="")
print()

with open(INDEX, "w") as file:
    file.write("const INDEX = ")
    json.dump(index, file, indent="  ")
    file.write(";")
