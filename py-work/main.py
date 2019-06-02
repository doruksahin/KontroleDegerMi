from googler import google_search

import tr_utils
import tokenizer, normalizer, stemmer, stopper

import locale
locale.setlocale(locale.LC_ALL,'en_US.UTF-8')

def parse(text):
    text = normalizer.normalize(text)
    tokens = tokenizer.tokenize(text)
    tokens = stopper.remove_stops(tokens)
    stemmed = stemmer.stem(tokens)
    filtered = stopper.remove_stops(stemmed)
    return filtered

text = "ama yani şimdi şöyle de bir olay var yani "
print((parse(text)))
