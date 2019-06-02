import nltk

_stop_words = set(nltk.corpus.stopwords.words("turkish"))
_stop_words.update(["olan", "bir", "aşağı", "hangi", "şimdi", "şöyle", "böyle"])

def remove_stops(tokens):
    return [token for token in tokens if token not in _stop_words]