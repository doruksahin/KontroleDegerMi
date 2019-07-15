import json
import sys

RESULT_FILE_PATH = ""
json_data = []

def write_json():
	global json_data
	global RESULT_FILE_PATH

	RESULT_FILE_PATH = "claims.json"

	'''
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
	'''

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


def write_txt():
	global json_data
	global RESULT_FILE_PATH

	RESULT_FILE_PATH = "claims.txt"

	f = open('teyit-org.json', 'r')
	j = json.load(f)
	for block in j:
		claim = ""
		if block['claim'] == None:
			claim = ""
		else:
			claim = block['claim']
		claim += " {}".format(block['claim_title'])
		json_data.append(claim)



	f = open('dogrula-org.json', 'r')
	j = json.load(f)
	for block in j:
		try:
			claim = block['claim']
		except:
			claim = ""
		claim += " {}".format(block['claim_title'])
		json_data.append(claim)


	f = open('dogrulukpayi-com.json', 'r')
	j = json.load(f)
	for block in j:
		claim = block['claim']
		json_data.append(claim)



	f = open('gununyalanlari-com.json', 'r')
	j = json.load(f)
	for block in j:
		claim = block['claim']
		claim += " {}".format(block['context'])
		json_data.append(claim)





if __name__ == '__main__':
	arg = sys.argv[1]
	if arg == "json":
		write_json()
	else:
		write_txt()

	with open(RESULT_FILE_PATH, 'w') as outfile:
		json.dump(json_data, outfile)