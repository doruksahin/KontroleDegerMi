import csv
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVC
from pprint import pprint
import json
import random
import sys
import pickle

test_input = sys.argv[1]
test_feature = sys.argv[2]
expected_data = sys.argv[3]
train_feature_claim = sys.argv[4]
train_feature_not_claim = sys.argv[5]

# for testing
with open(test_input, "r") as f:
	test_twits = json.load(f)

# for perfromance measue
with open(expected_data, "r") as f:
	expected_data = json.load(f)

expected_output = []
for x in expected_data:
	expected_output.append(x['is_checkworthy'])

train_data = []
is_claim = []
with open(train_feature_claim, "r") as f:
	reader = csv.reader(f, delimiter="\t")
	
	flag = True
	for line in reader:
		if flag:
			flag = False
			continue

		mini_train_data = [int(f) for f in line[0].split(",")]
		train_data.append(mini_train_data)
		is_claim.append(1)

with open(train_feature_not_claim, "r") as f:
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
with open(test_feature, "r") as f:
	reader = csv.reader(f, delimiter="\t")

	flag = True
	for line in reader:
		if flag:
			flag = False
			continue

		mini_test_data = [int(f) for f in line[0].split(",")]
		test_data.append(mini_test_data)

model = GaussianNB()
model.fit(train_data, is_claim)
pickle.dump(model, open("bayes_model.sav", "wb"))
predicted = model.predict(test_data)

#for i, pred in enumerate(predicted):
#	if pred == 1:
#		print("{}-{}-{}".format(i, pred, test_twits[i]))

#predicted = predicted[0:len(train_data)]
print(metrics.classification_report(expected_output, predicted))
print(metrics.confusion_matrix(expected_output, predicted))

#fiçur normalizatiosn? ve aradğer tahminleri
'''
dataset = datasets.load_iris()
print(dataset)
print(dataset.data)
model = GaussianNB()
model.fit(dataset.data, dataset.target)
expected = dataset.target
predicted = model.predict(dataset.data)
print(predicted)

print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
'''