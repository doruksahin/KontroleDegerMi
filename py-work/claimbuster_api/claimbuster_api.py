import urllib.parse
import json
import requests

filename = "test_input_translated.json"
link = "https://idir.uta.edu/factchecker/score_text/"
out_filename = "claimbuster_results.json"


def makine_kandirmaca(filename):
	f = open(filename)
	j = json.load(f)
	tweets = []
	for tweet in j:
		tweet = tweet.replace("?", "")
		tweet = tweet.replace(".", "")
		tweet = tweet.replace("!", "")
		tweets.append(tweet)
	return tweets


def write_file(score_array):
	with open(out_filename, 'w') as outfile:
		json.dump(score_array, outfile, indent=4)

if __name__ == '__main__':
	j = makine_kandirmaca(filename)
	score_array = []
	for tweet in j:
		block = {}
		encoded_tweet = urllib.parse.quote(tweet)
		full_link = link + encoded_tweet
		print(full_link)
		response = requests.get(full_link)
		print(json.dumps(response.json(), indent=4, sort_keys=True))
		score = float(response.json()['results'][0]['score'])
		print(score)
		print(type(score))
		if score < 0.5:
			score = 0
		else:
			score = 1
		block['tweet'] = tweet
		block['is_checkworthy'] = score
		score_array.append(block)
	write_file(score_array)

