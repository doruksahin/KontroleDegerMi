import nltk

def tokenize(text):
    return nltk.word_tokenize(text, 'turkish')