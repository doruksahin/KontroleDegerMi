g_posTypes = None
g_fullWords = None
g_stemmedWords = None

def _read_data_set():
    global g_posTypes
    global g_fullWords
    global g_stemmedWords
    g_posTypes = set()
    g_fullWords = dict()
    g_stemmedWords = dict()

    file = open("all.conllu", "r")
    for line in file:
        if line.startswith("#"):
            continue
        if len(line) == 0:
            continue
        values = line.split("\t")
        values.pop(0)
        if len(values) == 0:
            continue
        values.pop(2)
        values.pop(3)
        values.pop(3)
        values.pop(3)
        values.pop(3)
        values.pop(3)
        g_posTypes.add(values[2])
        g_fullWords[values[0]] = values[2]
        g_stemmedWords[values[1]] = values[2]

def get_pos(token):
    if token in g_fullWords:
        return g_fullWords[token]
    elif token in g_stemmedWords:
        return g_stemmedWords[token]
    else:
        return "_"

_read_data_set()

def convert_pos(tokens):
    return [get_pos(token) for token in tokens]

def get_column_names():
    row = []
    for column in g_posTypes:
        row.append(column)
    row.sort()
    return row

def extract_feature(tokens):
    tokens = convert_pos(tokens)
    row = []
    for column in get_column_names():
        count = 0
        for token in tokens:
            if token == column:
                count = count + 1
        row.append(count)
    return row
    