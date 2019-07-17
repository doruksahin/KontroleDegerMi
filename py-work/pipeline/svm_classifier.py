import csv
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVC
from pprint import pprint
import json
import random

# for testing
with open("test_input.json", "r") as f:
	test_twits = json.load(f)

# for perfromance measue
with open("expected.json", "r") as f:
	expected_data = json.load(f)

expected_output = []
for x in expected_data:
	expected_output.append(x['is_checkworthy'])

train_data = []
is_claim = []
with open("train_feature_claim.csv", "r") as f:
	reader = csv.reader(f, delimiter="\t")
	
	flag = True
	for line in reader:
		if flag:
			flag = False
			continue

		mini_train_data = [int(f) for f in line[0].split(",")]
		train_data.append(mini_train_data)
		is_claim.append(1)

with open("train_feature_not_claim.csv", "r") as f:
	reader = csv.reader(f, delimiter="\t")
	
	flag = True
	for line in reader:
		if flag:
			flag = False
			continue

		mini_train_data = [int(f) for f in line[0].split(",")]
		train_data.append(mini_train_data)
		is_claim.append(0)

test_data = []
with open("test_feature.csv", "r") as f:
	reader = csv.reader(f, delimiter="\t")

	flag = True
	for line in reader:
		if flag:
			flag = False
			continue

		mini_test_data = [int(f) for f in line[0].split(",")]
		test_data.append(mini_test_data)
		
model = SVC(kernel='linear', random_state=0, verbose=10000)
model.fit(train_data, is_claim)
predicted = model.predict(test_data)

#for i, pred in enumerate(predicted):
#	if pred == 1:
#		print("{}-{}-{}".format(i, pred, test_twits[i]))

#predicted = predicted[0:len(train_data)]
print(metrics.classification_report(expected_output, predicted))
print(metrics.confusion_matrix(expected_output, predicted))

