import requests
from bs4 import BeautifulSoup
import lxml

import time

def count_words(url):
    if "http" not in url:
        url = "http://" + url
    print(url)
    print(f"Counting words at {url}")
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser") #lxml
    word_count = dict()

    for i in soup.getText().split():
        i = i.lower().replace(",", " ").replace(".", " ").replace(";", " ").replace(":", " ").replace("(", " ")\
            .replace(")", " ").replace("/", " ").replace("-", " ").replace("?", " ").replace("!", " ")\
            .replace("[", " ").replace("]", " ").replace("\"", " ").replace("—", " ").replace("_", " ")\
            .replace("–", " ").replace("|", " ").replace(" ", "")
        if i == "":
            continue
        if not i in word_count:
            word_count[i] = 1
        else:
            word_count[i] += 1

    word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    word_count = dict(word_count)
    return word_count


# count_words("turk.net/hakkimizda/index/")
