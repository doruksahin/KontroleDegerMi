import json

g_all_words = []
#g_word_count = None

def prepare_words_list(tokens_array):
    all_words = set()
    word_count = dict()
    for tokens in tokens_array:
        for token in tokens:
            if token in word_count:
                word_count[token] = word_count[token] + 1
            else:
                word_count[token] = 0
            all_words.add(token)
    words = []
    for item in all_words:
        words.append(item)
    words = [word for word in all_words if word_count[word] > 5]
    words.sort()
    with open('words.txt', 'w') as f:
        json.dump(words, f)

with open('words.txt', 'r') as f:
    g_all_words = json.load(f)

def get_column_names():
    return g_all_words

def extract_feature(tokens):
    result = []
    for word in g_all_words:
        count = 0
        for token in tokens:
            if token == word:
                count = count + 1
        result.append(count)
    return result