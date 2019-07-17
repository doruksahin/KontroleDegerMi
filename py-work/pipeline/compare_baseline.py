import sys
import json
import csv
from sklearn import metrics

baseline_output = []
with open(sys.argv[1], "r") as f:
    baseline_json = json.load(f)
    for item in baseline_json:
        baseline_output.append(item["is_checkworthy"])

expected_output = []
with open(sys.argv[2], "r") as f:
    expected_json = json.load(f)
    for item in expected_json:
        expected_output.append(item["is_checkworthy"])
    
print(metrics.classification_report(expected_output, baseline_output))
print(metrics.confusion_matrix(expected_output, baseline_output))
