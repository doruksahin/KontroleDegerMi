import zemberek.nertagger
import locale
locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
import jpype as jp
import json

# ZEMBEREK_PATH = 'zemberek/bin/zemberek-full.jar'
# jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

if __name__ == '__main__':
	# Start the JVM
	
	zemberek.nertagger.init_libs()
	zemberek.nertagger.ner_tagging("Ali ata bak")


def extract_feature(tokens):
	appended_str = ""
	for token in tokens:
		appended_str += token + " "
	appended_str = appended_str[:-1]
	features = zemberek.nertagger.ner_tagging(appended_str)
	feature_vector = [0, 0, 0]
	for feature in features:
		if feature == "LOCATION":
			feature_vector[0] += 1
		elif feature == "ORGANIZATION":
			feature_vector[1] += 1
		elif feature == "PERSON":
			feature_vector[2] += 1
	return feature_vector

# jp.shutdownJVM()