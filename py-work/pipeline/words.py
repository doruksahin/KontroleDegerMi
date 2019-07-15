g_all_words = None
g_word_count = None

def prepare_data_set(tokens_array):
    global g_all_words
    global g_word_count
    all_words = set()
    g_word_count = dict()
    for tokens in tokens_array:
        for token in tokens:
            if token in g_word_count:
                g_word_count[token] = g_word_count[token] + 1
            else:
                g_word_count[token] = 0
            all_words.add(token)
    g_all_words = []
    for item in all_words:
        g_all_words.append(item)
    g_all_words = [word for word in g_all_words if g_word_count[word] > 5]
    g_all_words.sort()
    g_word_count = {key:val for key, val in g_word_count.items() if val > 5}

def extract_features(tokens):
    result = []
    for word in g_all_words:
        count = 0
        for token in tokens:
            if token == word:
                count = count + 1
        result.append(count)
    return result