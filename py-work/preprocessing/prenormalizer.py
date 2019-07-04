import string

def lower_case(text):
    return text.replace("I", 'ı').replace("İ", "i").lower()

def no_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def prenormalize(text):
    return no_punctuation(lower_case(text))