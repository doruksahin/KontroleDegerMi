import tr_utils
import tokenizer, prenormalizer, normalizer, stemmer, stopper

import locale
locale.setlocale(locale.LC_ALL,'en_US.UTF-8')

def parse(text):
    text = prenormalizer.prenormalize(text)

    tokens = tokenizer.tokenize(text)
    tokens = normalizer.normalize(tokens)
    tokens = stopper.remove_stops(tokens)
    stemmed = stemmer.stem(tokens)
    filtered = stopper.remove_stops(stemmed)
    return filtered

text = "   tamm    iyi de .ama yani; şimdi \"şöyle\" de bir olay var yani "
print((parse(text)))
print((parse(text)))
print((parse(text)))
print((parse(text)))
print((parse(text)))
print((parse(text)))
print((parse(text)))
