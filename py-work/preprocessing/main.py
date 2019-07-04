import tr_utils
import tokenizer, zemberek.normalizer, stemmer, stopper

import locale
locale.setlocale(locale.LC_ALL,'en_US.UTF-8')

def parse(text):
    text = zemberek.normalizer.normalize(text)
    tokens = tokenizer.tokenize(text)
    tokens = stopper.remove_stops(tokens)

    #stemmed = stemmer.stem(tokens)
    
    tokens = stopper.remove_stops(tokens)
    return tokens

text = "Hocam 3 gün geçiktirdiğimizde 3 kişilik bi grup ta herkezten bigün mü siliencek (1 * 3  = 3) yoksa herkesten mi 3 gün silinecek??"
print(parse(text))