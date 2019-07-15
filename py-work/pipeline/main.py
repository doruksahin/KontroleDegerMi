import sys
import json
import jpype as jp
import length, ner_tagging, pos_tagging
import csv
import zemberek.normalizer

# Start the JVM
ZEMBEREK_PATH = 'zemberek/bin/zemberek-full.jar'
jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

import preprocessing

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
    with open(output_file, mode='w') as feature_file:
        fieldnames = ['length', 'LOCATION', 'ORGANIZATION', 'PERSON', 'O'] + pos_columns
        writer = csv.writer(feature_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(fieldnames)
        count = 0
        for tokens in json_file:
            length_vector = length.extract_feature(tokens)
            ner_vector = ner_tagging.extract_feature(tokens) 
            pos_vector = pos_tagging.extract_feature(tokens)
            writer.writerow(length_vector + ner_vector + pos_vector)
            print(count)
            count = count + 1

if __name__ == '__main__':
    main()

jp.shutdownJVM()
