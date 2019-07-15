import zemberek.nertagger
import locale
locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
import jpype as jp
import json

if __name__ == '__main__':
	# Start the JVM
	ZEMBEREK_PATH = 'zemberek/bin/zemberek-full.jar'
	jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))
	
	zemberek.nertagger.init_libs()

	zemberek.nertagger.ner_tagging("Ali İzmir'e en son talip olanlar giderken")

	jp.shutdownJVM()