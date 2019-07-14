g_posTypes = None
g_fullWords = None
g_stemmedWords = None

def read_data_set():
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

def convert_pos(tokens):
    return [get_pos(token) for token in tokens]

read_data_set()

deneme = ['sonuç', 'açık', '24', 'haziran', '12', 'kadar', 'onay', 'işlem', 'haber', 'mağdur', 'mağduriyet', 'gider']
for item in deneme:
    print(item, ":", get_pos(item))
