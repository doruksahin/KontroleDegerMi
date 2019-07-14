import json

f = open('malumatfurus-org.json', 'r')
j = json.load(f)
for block in j:
	# print(block['claim_title'])
	print(block['claim'])