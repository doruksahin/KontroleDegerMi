#from snowballstemmer import TurkishStemmer
from TurkishStemmer import TurkishStemmer

def stem(tokens):
    stem = TurkishStemmer()
    stemmedTokens = []
    for w in tokens:
        stemmedTokens.append(stem.stem(w))
    return stemmedTokens