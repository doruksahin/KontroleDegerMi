import sys
import json
import jpype as jp
import length, ner_tagging, pos_tagging
import csv
import zemberek.normalizer
import words

# Start the JVM
ZEMBEREK_PATH = 'zemberek/bin/zemberek-full.jar'
jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

import preprocessing

USE_LENGTH = True
USE_POS = True
USE_NER = True
USE_BOW = False

def main():
    op = sys.argv[1]
    input = sys.argv[2]
    output = sys.argv[3]
    if op == "preprocess":
        preprocess(input, output)
    elif op == "extract-feature":
        extract_feature(input, output)
    else:
        pass

def preprocess(input_file, output_file):
    zemberek.normalizer.init()
    
    file = open(input_file, "r")
    content = file.read()
    data = json.loads(content)
    result = []
    count = 1
    for item in data:
        result.append(preprocessing.perform_preprocessing(item))
        count = count + 1
        print(count)
    with open(output_file, "w") as outfile:
        json.dump(result, outfile, indent=4)


def extract_feature(input_file, output_file):
    zemberek.nertagger.init_libs()

    f = open(input_file, 'r')
    json_file = json.load(f)

    pos_columns = pos_tagging.get_column_names()
    word_columns = words.get_column_names()
    with open(output_file, mode='w') as feature_file:
        fieldnames = []
        if USE_LENGTH:
            fieldnames = fieldnames + ['length']
        if USE_NER:
            fieldnames = fieldnames + ['LOCATION', 'ORGANIZATION', 'PERSON', 'O']
        if USE_POS:
            fieldnames = fieldnames + pos_columns
        if USE_BOW:
            fieldnames = fieldnames + word_columns
        writer = csv.writer(feature_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(fieldnames)
        count = 0
        for tokens in json_file:
            the_row = []
            if USE_LENGTH:
                length_vector = length.extract_feature(tokens)
                the_row = the_row + length_vector
            if USE_NER:
                ner_vector = ner_tagging.extract_feature(tokens) 
                the_row = the_row + ner_vector
            if USE_POS:
                pos_vector = pos_tagging.extract_feature(tokens)
                the_row = the_row + pos_vector
            if USE_BOW:
                bow_vector = words.extract_feature(tokens)
                the_row = the_row + bow_vector
            writer.writerow(the_row)
            print(count)
            count = count + 1

if __name__ == '__main__':
    main()

jp.shutdownJVM()
