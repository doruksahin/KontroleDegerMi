import json
import sys

filename = sys.argv[1]
f = open(filename, "r")
json_file = json.load(f)

length = len(json_file)


j = []
for i in range(int(length/3)):
	j.append(json_file[i])
with open("ali.json", 'w') as outfile:
    json.dump(j, outfile, indent=4)

j = []
for i in range(int(length/3), int((2*length)/3)):
	j.append(json_file[i])
with open("said.json", 'w') as outfile:
    json.dump(j, outfile, indent=4)

j = []
for i in range(int((2*length)/3), length):
	j.append(json_file[i])
with open("doruk.json", 'w') as outfile:
    json.dump(j, outfile, indent=4)
