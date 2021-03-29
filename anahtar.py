import requests
from bs4 import BeautifulSoup


def key_words(url):
    if "http" not in url:
        url = "http://" + url
    print(f"Counting words at {url}")

    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")  # lxml
    word_count = dict()
    for i in soup.getText().split():
        i = i.lower().replace(",", " ").replace(".", " ").replace(";", " ").replace(":", " ").replace("(", " ") \
            .replace(")", " ").replace("/", " ").replace("-", " ").replace("?", " ").replace("!", " ") \
            .replace("[", " ").replace("]", " ").replace("\"", " ").replace("—", " ").replace("_", " ") \
            .replace("–", " ").replace("|", " ").replace(" ", "")
        if i == "":
            continue
        if not i in word_count:
            word_count[i] = 1
        else:
            word_count[i] += 1

    word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    if len(word_count) > 5:
        word_count = word_count[:5]  # anahtar kelimeler listenin ilk 5 elemanı

    word_count = dict(word_count)
    return word_count

# key_words("https://turk.net/hakkimizda/index/")
