import sys
import json
import jpype as jp

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
    pass

if __name__ == '__main__':
    main()

jp.shutdownJVM()
