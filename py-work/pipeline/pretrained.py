import csv
from sklearn import datasets
from sklearn import metrics
from sklearn.svm import SVC
from pprint import pprint
import json
import random
import sys
import pickle
import preprocessing
import jpype as jp
import zemberek.normalizer
import length, ner_tagging, pos_tagging
import csv
import words

######################## Prepare for preprocessing
ZEMBEREK_PATH = 'zemberek/bin/zemberek-full.jar'
jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))
zemberek.normalizer.init()
zemberek.nertagger.init_libs()

######################## Load pretrained model
model = pickle.load(open("svm_model.sav", "rb"))

def extract_feature(tokens):
    pos_columns = pos_tagging.get_column_names()
    word_columns = words.get_column_names()

    fieldnames = []
    fieldnames = fieldnames + ['length']
    fieldnames = fieldnames + ['LOCATION', 'ORGANIZATION', 'PERSON', 'O']
    fieldnames = fieldnames + pos_columns
    #fieldnames = fieldnames + word_columns
    
    the_row = []
    length_vector = length.extract_feature(tokens)
    the_row = the_row + length_vector
    ner_vector = ner_tagging.extract_feature(tokens) 
    the_row = the_row + ner_vector
    pos_vector = pos_tagging.extract_feature(tokens)
    the_row = the_row + pos_vector
    #bow_vector = words.extract_feature(tokens)
    #the_row = the_row + bow_vector
    return the_row

while True:
    test_string = input("Please enter some input:\n")
    preprocessed = preprocessing.perform_preprocessing(test_string)
    feature_vector = extract_feature(preprocessed)

    test_data = []
    test_data.append(feature_vector)

    predicted = model.predict_proba(test_data)
    print("Prob(Check-Worthy) =", predicted[0][1])