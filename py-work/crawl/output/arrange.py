import json




RESULT_FILE_PATH = "claims.json"
json_data = []


f = open('malumatfurus-org.json', 'r')
j = json.load(f)
for block in j:
	json_block = {}
	json_block['claim'] = block['claim']
	# print(json_block['claim'])
	json_block['claim'] += " {}".format(block['claim_title'])
	json_block['date'] = block['date']
	json_block['source'] = "malumatfurus_org"
	json_data.append(json_block)


f = open('teyit-org.json', 'r')
j = json.load(f)
for block in j:
	json_block = {}
	if block['claim'] == None:
		json_block['claim'] = ""
	else:
		json_block['claim'] = block['claim']
	json_block['claim'] += " {}".format(block['claim_title'])
	json_block['date'] = block['date']
	json_block['source'] = "teyit_org"
	json_data.append(json_block)


f = open('dogrula-org.json', 'r')
j = json.load(f)
for block in j:
	json_block = {}
	try:
		json_block['claim'] = block['claim']
	except:
		json_block['claim'] = ""
	json_block['claim'] += " {}".format(block['claim_title'])
	json_block['date'] = block['date']
	json_block['source'] = "dogrula_org"
	json_data.append(json_block)


f = open('dogrulukpayi-com.json', 'r')
j = json.load(f)
for block in j:
	json_block = {}
	json_block['claim'] = block['claim']
	json_block['date'] = block['date']
	json_block['source'] = "dogrulukpayi_com"
	json_data.append(json_block)


f = open('gununyalanlari-com.json', 'r')
j = json.load(f)
for block in j:
	json_block = {}
	json_block['claim'] = block['claim']
	json_block['claim'] += " {}".format(block['context'])
	json_block['date'] = block['date']
	json_block['source'] = "gununyalanlari_com"
	json_data.append(json_block)





with open(RESULT_FILE_PATH, 'w') as outfile:
	json.dump(json_data, outfile, indent=4)