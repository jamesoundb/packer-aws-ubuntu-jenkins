#! /usr/bin/env python3
import json

json_file = "../packer-manifest.json"

def ami(file):
    """Parses packer-manifest json file and returns region and latest build AMI ID"""
    with open(file, "r") as file:
        f = file.read()
        manifest = json.loads(f)
        for k, v in manifest.items():
            if k == "builds":
                last_build = v[-1]
                image = last_build.get("artifact_id").split(":")
                print(f"Region: {image[0]} \nImage: {image[1]}")


if __name__ == '__main__':
    ami(json_file)
