import zemberek.nertagger
import locale
locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
import jpype as jp
import json


json_file = "ornek.json"


def train_ner_model():
	zemberek.nertagger.train_ner()


def ner_tagging(sentence):
	zemberek.nertagger.ner_tagging(sentence)


if __name__ == '__main__':
	# Start the JVM
	ZEMBEREK_PATH = 'zemberek/bin/zemberek-full.jar'
	jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))
	
	zemberek.nertagger.init_libs()
	# train_ner_model()

	f = open(json_file, 'r')
	j = json.load(f)
	for tweet in j:
		ner_tagging(tweet)

	jp.shutdownJVM()