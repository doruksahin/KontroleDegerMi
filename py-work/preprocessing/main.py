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

text = "Çiftlik Bank davasında mahkeme iki sanığın tahliyesine karar verdi. Böylece dava kapsamında tutuklu sanık kalmadı"
print(perform_preprocessing(text))

jp.shutdownJVM()