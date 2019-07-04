import tokenizer, zemberek.normalizer, zemberek.stemmer, stopper

import locale
locale.setlocale(locale.LC_ALL,'en_US.UTF-8')

import jpype as jp

# Start the JVM
ZEMBEREK_PATH = 'zemberek/bin/zemberek-full.jar'
jp.startJVM(jp.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

def perform_preprocessing(text):
    text = zemberek.normalizer.normalize(text)
    tokens = tokenizer.tokenize(text)
    tokens = stopper.remove_stops(tokens)
    tokens = zemberek.stemmer.stem_words(tokens)
    tokens = stopper.remove_stops(tokens)
    return tokens

text = "Hocam 3 gün geçiktirdiğimizde 3 kişilik bi grup ta herkezten bigün mü siliencek (1 * 3  = 3) yoksa herkesten mi 3 gün silinecek??"
print(perform_preprocessing(text))

jp.shutdownJVM()