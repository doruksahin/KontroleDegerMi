#import ..\py-work\preprocessing\main

#preprocessing metodu burada kullanilcak. import edilcek.


def feature_length(text):
    tokens = perform_preprocessing(text)
    return len(tokens)


def feature_words():
    wordPool = {}
    #buraya text'lerin liste seklinde verilecegini varsaydim.
    #aslinda kelimeler degil token'larin gelmesi gerekiyor.
    wordList = []
    wordList.append("Android bir bir bir bir bir markette markette Pazarda markette kahvede herkes EYT i konuşuyor asıl ittifakı biz kurduk hakkımızı istiyoruz #ÖnceMilletDiyorsanızEYT")
    wordList.append("Bir gün Norveç'te markette markette kitapçıdan kitaplarını kitaplarını aldıktan sonra kuzey ışıklarını izlemek için karla kaplı dağlara çıkmayı bekleyen bir hayalperest.")
    for tweet in wordList:
        words = tweet.lower().split()
        for word in words:
            word = word.replace(",","")
            word = word.replace(".","")
            if word in wordPool:
                wordPool[word] = wordPool[word] + 1
            else:
                wordPool[word] = 1

    # tum kelimelerin frekanslarini kucukten buyuge siraliyor. 
    wordPool = (sorted(wordPool.items(), key=lambda x: x[1]))
    # buyukten kucuge siralamak icin: " , reverse=True"  eklenmeli.


    # frekansi 5'ten kucuk tum kelimeleri siliyorum. (hassan da oyle yapmisti)
    silinecekFrekans = 5
    wordPool = [x for x in wordPool if x[1] >= silinecekFrekans]

    uzunluk = len(wordPool)
    #ornegin elimizde toplam 100.000 kelime kaldi.
    #en az ve en cok gecen kelimeler silinecek
    #en az gecen %20 ve en cok gecen %10 yi sildigimizi varsaydim, degisebilir.
    # %20 - %90 arasını almak icin relative kod yaziyorum.

    az = 20   #   silinecekAzGecenKelimeOrani  %20
    cok = 10  #   silinecekCokGecenKelimeOrani %10

    #print(int(uzunluk*az/100))
    #print(uzunluk - int(uzunluk*cok/100))

    wordPool = wordPool[ int(uzunluk*az/100) : uzunluk - int(uzunluk*cok/100) ]

    #tuple' in icindeki kalan tum kelimeler birer feature. (words feature)

    return wordPool


def POS():
    return 0

def sentiment():
    return 0

def entityType():
    return 0