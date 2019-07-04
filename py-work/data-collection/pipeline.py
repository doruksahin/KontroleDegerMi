import os
import codecs
import io
import json




path = 'C:\\Users\\msaidzengin\\Desktop\\tweets'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))



for i in range(len(files)):
    print(i)
    with open(files[i], encoding="utf8") as f:
        content = f.readlines()
    f.close()

    tweets = []
    for line in content:
        bol = line.split("\t")
        tweets.append(bol[8])

    jsonTweet = json.dumps(tweets)
    with io.open("C:\\Users\\msaidzengin\\Desktop\\twitler\\"+str(i)+".txt", 'w', encoding='utf8') as file:
        file.write(jsonTweet)
    file.close()