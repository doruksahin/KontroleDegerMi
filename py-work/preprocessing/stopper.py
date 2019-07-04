import nltk

_stop_words = set(nltk.corpus.stopwords.words("turkish"))
_stop_words.update(["olan", "bir", "aşağı", "hangi", "şimdi", "şöyle", "böyle"])
_stop_words.update(["tamam", "iyi", "ta", "mı", "mi"])

def remove_stops(tokens):
    return [token for token in tokens if token not in _stop_words]