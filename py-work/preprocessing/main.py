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

text = "Sonuçların açıklandığı 24 haziranda 12ye kadar onay red işlemi yapılıyormuş.. Bundan haberi olmayanlar mağdur oldu. Bu mağduriyet giderilmelidir.. #2019ildışıiptalhakkı"
print(perform_preprocessing(text))

jp.shutdownJVM()