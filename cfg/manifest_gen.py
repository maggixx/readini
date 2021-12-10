import json

name = input("Project name: ")
desc = input("Description: ")
version = input("Version: ")
license = input("License: ")
created = input("Created: ")

jsonb = {
  "name": f"{name}",
  "desc": f"{desc}",
  "version": f"{version}",
  "license": f"{license}",
  "created": f"{created}"
}

a = json.dumps(jsonb)

with open("output.json", "w") as f:
  f.write(a)