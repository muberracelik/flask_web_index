import requests
from bs4 import BeautifulSoup
from anahtar import key_words

html_liste = []
oran_liste = []
html_text = ""
kelimeler = None
kelimesozluk = dict()
with open("esanlamlikelimeler.txt") as f:
    kelimeler = f.readlines()
for kelime in kelimeler:
    kelime1, kelime2 = kelime.split(",")
    kelimesozluk[kelime1] = kelime2
    kelimesozluk[kelime2] = kelime1


def alt_link(ana_url, kume_url):
    html = requests.get(kume_url)
    soup = BeautifulSoup(html.content, "html.parser")
    urls = set()
    base = "//" + kume_url.split("/")[2]
    for link in soup.find_all('a'):
        if "http" in str(link.get('href')) and base in str(link.get('href')):
            urls.add(link.get('href'))
    print(urls)
    oran = 0
    kume_oran = 0
    ana_oran = 0
    anahtar1 = key_words(ana_url)
    anahtar3 = key_words(kume_url)
    tmp_liste = []
    tmp_oran_liste = []
    for link in urls:
        tmp = ""
        if link in ["NULL", "_blank", "None", None, "NoneType", kume_url]:
            continue
        anahtar2 = key_words(link)
        bo = benzerlik_orani(anahtar1, anahtar2)
        kume_oran += bo
        tmp = "-\t\t" + link + " Benzerlik Oranı => " + str(bo) + "\t keywords: " + str(anahtar2) + "\n"
        tmp_liste.append(tmp)
        tmp_oran_liste.append(bo)
    n = len(tmp_liste)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if tmp_oran_liste[j] < tmp_oran_liste[j + 1]:
                tmp_oran_liste[j], tmp_oran_liste[j + 1] = tmp_oran_liste[j + 1], tmp_oran_liste[j]
                tmp_liste[j], tmp_liste[j + 1] = tmp_liste[j + 1], tmp_liste[j]
    tmp = ""
    for i in range(len(tmp_liste)):
        tmp += tmp_liste[i] + "\n"
    kume_oran = kume_oran / len(urls)
    ana_oran = benzerlik_orani(anahtar1, anahtar3)
    oran = (kume_oran * 40 / 100) + (ana_oran * 60 / 100)
    oran = round(oran, 2)
    return anahtar3, tmp, oran


def indexle_sirala1(ana_url, kume_url):
    html_text = ""
    kume_urller = kume_url.split("\n")
    anahtar1 = key_words(ana_url)
    if anahtar1 == "BU SİTE İÇİN İŞLEM YAPILAMIYOR":
        raise Exception("BU SİTE İÇİN İŞLEM YAPILAMIYOR")
    key1_es = dict()
    for i in range(len(anahtar1)):
        kelime_tmp = str(list(anahtar1.keys())[i])
        es_kelime = kelimesozluk.get(kelime_tmp)
        if es_kelime != None:
            es_kelime = str(es_kelime)
            key1_es[es_kelime.replace("\n","")] = int(str(list(anahtar1.values())[i]))
    html_text += "Ana Url = " + ana_url + " " + str(anahtar1) + " Eş anlamlılar: " +str(key1_es) + "\n\n"
    print(html_text)
    if "" in kume_urller:
        kume_urller.remove("")
    for link in kume_urller:
        text = ""
        anahtar3, tmp, oran = alt_link(ana_url, link)
        text += "+\t" + str(link) + " Genel Skor => " + str(oran) + "\t Anahtar Kelimeler: " + str(
            anahtar3) + "\n" + tmp
        oran_liste.append(oran)
        html_liste.append(text)
    n = len(html_liste)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if oran_liste[j] < oran_liste[j + 1]:
                oran_liste[j], oran_liste[j + 1] = oran_liste[j + 1], oran_liste[j]
                html_liste[j], html_liste[j + 1] = html_liste[j + 1], html_liste[j]
    for i in range(len(html_liste)):
        html_text += html_liste[i] + "\n"

    return html_text


def benzerlik_orani(key1, key2):
    try:
        benzer_sayi = 0
        farkli_sayi = 0
        toplam_sayi = len(key1)
        kelime_benzerlik_orani = 0
        katsayi_benzerlik_orani = 0
        benzerlik_oran = 0

        key1_es = dict()
        for i in range(len(key1)):
            kelime_tmp = str(list(key1.keys())[i])
            es_kelime = kelimesozluk.get(kelime_tmp)
            if es_kelime != None:
                es_kelime = str(es_kelime)
                key1_es[es_kelime.replace("\n", "")] = int(str(list(key1.values())[i]))
            print(es_kelime)

        for i in range(len(key1)):
            varmi = False
            for j in range(len(key2)):
                if list(key1.keys())[i] in list(key2.keys())[j]:
                    benzer_sayi += 1
                    varmi = True
                    if int(str(list(key1.values())[i])) > int(str(list(key2.values())[j])):
                        katsayi_benzerlik_orani += int(str(list(key2.values())[j])) / int(
                            str(list(key1.values())[i])) * 100
                    else:
                        katsayi_benzerlik_orani += int(str(list(key1.values())[i])) / int(
                            str(list(key2.values())[j])) * 100
                try:
                    if list(key1_es.keys())[i] in list(key2.keys())[j]:
                        benzer_sayi += 1
                        varmi = True
                        if int(str(list(key1_es.values())[i])) > int(str(list(key2.values())[j])):
                            katsayi_benzerlik_orani += int(str(list(key2.values())[j])) / int(
                                str(list(key1_es.values())[i])) * 100
                        else:
                            katsayi_benzerlik_orani += int(str(list(key1_es.values())[i])) / int(
                                str(list(key2.values())[j])) * 100
                except:
                    continue

            if varmi is False:
                farkli_sayi += 1

        for i in range(len(key2)):
            varmi = False
            for j in range(len(key1)):
                if list(key1.keys())[j] in list(key2.keys())[i]:
                    varmi = True
            if varmi is False:
                farkli_sayi += 1

        kelime_benzerlik_orani = 100 - (farkli_sayi / toplam_sayi / 2 * 100)
        katsayi_benzerlik_orani = katsayi_benzerlik_orani / toplam_sayi
        benzerlik_oran = (katsayi_benzerlik_orani + kelime_benzerlik_orani) / 2
        benzerlik_oran = round(benzerlik_oran, 2)
        print(benzerlik_oran)
        return benzerlik_oran
    except:
        return 0.0
