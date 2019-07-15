import csv
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from pprint import pprint


train_data = []
is_claim = []			# Since our train_data full of claims, its all 1
with open("train_feature.csv", "r") as f:
	reader = csv.reader(f, delimiter="\t")
	
	flag = True
	for line in reader:
		if flag:
			flag = False
			continue

		mini_train_data = [int(f) for f in line[0].split(",")]
		train_data.append(mini_train_data)
		is_claim.append(1)

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



model = GaussianNB()
model.fit(train_data, is_claim)
predicted = model.predict(test_data)

for i, pred in enumerate(predicted):
	print("{}-{}".format(i, pred))

print(type(predicted))



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