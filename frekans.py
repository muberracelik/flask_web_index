import requests
from bs4 import BeautifulSoup


def count_words(url):
    try:
        if "http" not in url:
            url = "http://" + url
        print(url)
        print(f"Counting words at {url}")
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")  # lxml
    except:
        return "BU SİTE İÇİN İŞLEM YAPILAMIYOR"


    word_count = dict()
    baglaclar = ["için", "gibi", "kadar", "bir", "ancak", "yalnız", "ile", "sadece", "sanki", "değil", "üzere", "mi",
                 "rağmen",
                 "diye", "beri", "dek", "göre", "dair", "karşı", "karşın", "özgü", "doğru", "değin", "ait", "başka",
                 "itibaren",
                 "dolayı", "ötürü", "adeta", "sırf", "tek", "ve", "ama", "fakat", "lakin", "ki",
                 "de", "da", "den", "dan", "oysaki", "halbuki", "ne", "mı", "mu", "mü", "hem", "hep", "dedi", "ise",
                 "veya", "veyahut", "", "nasıl", "nedir", "biz", "siz", "onlar", "bu", "şu", "o", "ben", "sen",
                 "bizler",
                 "sizler", "tüm", "bütün", "hep", "her", "şey", "bize", "ya", "ye", "0", "1", "2", "3", "4", "5", "6",
                 "7", "8", "9",
                 "daha", "tamamı", "tamam", "eğer", "yok", "herhangi", "çok", "yoksa", "bende", "sende", "az", "tabi",
                 "olsa", "tabiki", "şuan", "evet", "hayır", "öyle", "böyle", "şöyle", "halinde", "bi", "peki", "an",
                 "yine", "miyiz",
                 "mıyız", "bizde", "sizde", "arada", "lütfen", "bizi", "sizi", "illa", "kesin", "önce", "sonra", "ilk",
                 "son"]

    for i in soup.getText().split():
        try:
            i = i.lower().replace(",", " ").replace(".", " ").replace(";", " ").replace(":", " ").replace("(", " ") \
                .replace(")", " ").replace("/", " ").replace("-", " ").replace("?", " ").replace("!", " ") \
                .replace("[", " ").replace("]", " ").replace("\"", " ").replace("—", " ").replace("_", " ") \
                .replace("–", " ").replace("|", " ").replace(" ", "")
            baglacmi = False
            for baglac in baglaclar:
                if baglac == i:
                    baglacmi = True
                    break
            if baglacmi is True:
                continue
            if not i in word_count:
                word_count[i] = 1
            else:
                word_count[i] += 1
        except:
            continue

    word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    word_count = dict(word_count)
    return word_count


