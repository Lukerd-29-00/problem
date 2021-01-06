from os import system
import requests
import json

base = "http://localhost:7200/rest"

r = requests.delete(base + "/repositories/Rainmaker")

print(r.text)

cmd = "curl -XPOST " + base + "/repositories -H 'Content-Type:multipart/form-data' -F \"config=@config.ttl\""
print(cmd)
system(cmd)
#f = open("config.ttl")
#r = requests.post(base + "/repositories",files={'config':f})

print(r.text)

system("cp /mnt/c/Users/Lucas/Documents/VSCODE/transfer_47077_files_f2c1d4be/* /mnt/c/Users/Lucas/graphdb-import")
system("./getfiles")
f=open("output.txt")
o = f.readlines()
f.close()
system("rm -f output.txt")

o = [x.strip() for x in o]

o = json.dumps(o)

print(o)

r = requests.post("http://localhost:7200/rest/data/import/server/Rainmaker",headers={"Content-Type": "application/json","Accept":"application/json"},data='{"fileNames":' + o + "}")

print(r.text)

