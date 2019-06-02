import json
from os import listdir, makedirs
from os.path import isfile, join

# Bu program json dosyalarindaki postlari paylasan kisinin post'a yazdigi yazilari extract eder.

def get_posts(filename):
    with open(filename, 'r') as file_json:
        myJson = json.load(file_json)
        texts = []
        for content in myJson['contents']:
        	if content['description'] != None:
        		texts.append(content['description'].encode("utf-8"))
        	# for comment in content['comments']:
        	# 	texts.append(comment['comment'])
    return texts






files = [f for f in listdir("./") if (isfile(join("./", f)) & (".json" in f))]
print(files)


for filename in files:
	textArr = get_posts(filename)
	with open(filename[:-5] + ".txt", "w") as f:
		for text in textArr:
			f.write(text + "\n")