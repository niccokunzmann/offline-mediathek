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

index = {}
for path, dirnames, fnames in os.walk(CONTENT):
    for fname in fnames:
        fid, ext = os.path.splitext(fname)
        index.setdefault(fid, {})
        entry = index[fid]
        entry_path = os.path.join(path, fname)
        add[ext](entry, entry_path)
        print(".", end="")

with open(INDEX, "w") as file:
    json.dump(index, file)
