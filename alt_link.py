import requests
from bs4 import BeautifulSoup


def alt_link(base_url):
    base_url = "https://turk.net/hakkimizda/index/"
    html = requests.get(base_url)
    soup = BeautifulSoup(html.content, "html.parser")

    urls = set()
    base = "//" + base_url.split("/")[2]
    for link in soup.find_all('a'):
        if "http" in str(link) and base in str(link):
            urls.add(link.get('href'))
    print(urls)

    words = 0
    for url in urls:
        if url in ["NULL", "_blank", "None", None, "NoneType", base_url]:
            continue

        # The == base_url case is handled in the above `if`
        if url[0] == "/":
            specific_url = base_url + url  # requests.get does not care about the num of '/'
        else:
            specific_url = url

        r = requests.get(specific_url)
        soup = BeautifulSoup(r.text, features="html.parser")
        for script in soup(["script", "style"]):
            # Use clear rather than extract
            script.clear()
        # text is text you don't need to preprocess it just yet.
        text = soup.get_text()
        print(f"{specific_url}: {len(text)} words")
        words += len(text)

    print(f"Total: {words} words")
