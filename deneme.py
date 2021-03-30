import requests
from bs4 import BeautifulSoup
from benzerlik import benzerlik_orani
from anahtar import key_words

html_liste = []
oran_liste = []
html_text = ""


def alt_link(ana_url, kume_url):
    tmp = ""
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
    for link in urls:
        if link in ["NULL", "_blank", "None", None, "NoneType", kume_url]:
            continue
        anahtar2 = key_words(link)
        bo = benzerlik_orani(anahtar1, anahtar2)
        kume_oran += bo
        tmp += "\t\t" + link + " Benzerlik Oranı: " + str(bo) + "\t keywords: " + str(anahtar2) + "\n"
    kume_oran = kume_oran / len(urls)
    ana_oran = benzerlik_orani(anahtar1, anahtar3)
    oran = (kume_oran * 40 / 100) + (ana_oran * 60 / 100)

    return anahtar3, tmp, oran


def indexle_sirala(ana_url, kume_url):
    """"
https://turk.net/cevre-politikasi
https://turk.net/destek
"""
    html_text = ""
    ana_url = "https://turk.net/hakkimizda/altyapimiz/"
    kume_url = "https://turk.net/destek\nhttps://turk.net/cevre-politikasi\n"
    kume_urller = kume_url.split("\n")
    anahtar1 = key_words(ana_url)
    html_text += "Ana Url = " + ana_url + str(anahtar1) + "\n\n"
    if "" in kume_urller:
        kume_urller.remove("")
    for link in kume_urller:
        text = ""
        anahtar3, tmp, oran = alt_link(ana_url, link)
        text += "\t"+str(link) + " Genel Skor => " + str(oran) + "\t keywords: " + str(anahtar3) + "\n" + tmp
        oran_liste.append(oran)
        html_liste.append(text)
    n = len(html_liste)
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if oran_liste[j] < oran_liste[j + 1]:
                oran_liste[j], oran_liste[j + 1] = oran_liste[j + 1], oran_liste[j]
                html_liste[j], html_liste[j + 1] = html_liste[j + 1], html_liste[j]
    for i in range(len(html_liste)):
        html_text += html_liste[i]+"\n"
    print(html_text)




indexle_sirala("gsdf", "fgsd")
