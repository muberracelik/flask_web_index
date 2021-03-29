from flask import Flask, render_template, request, redirect
from frekans import count_words
from anahtar import key_words
from benzerlik import benzerlik_orani
from indexleme import indexle_sirala

app = Flask(__name__)
app.debug = True


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/frekans_hesaplama', methods=['GET', 'POST'])
def frekans_hesaplama():
    web = None
    if request.method == 'POST':
        web = request.form['url']
        web = count_words(web)
        print(web)
    return render_template("frekans_hesaplama.html", web=web)


@app.route("/anahtar_kelime", methods=['GET', 'POST'])
def anahtar_kelime():
    web = None
    if request.method == 'POST':
        web = request.form['url']
        web = key_words(web)
        print(web)
    return render_template("anahtar_kelime.html", web=web)


@app.route("/benzerlik_skorlamasi", methods=['GET', 'POST'])
def benzerlik_skorlamasi():
    web1 = None
    web2 = None
    key1 = None
    key2 = None
    oran = None
    if request.method == 'POST':
        web1 = request.form['url1']
        web2 = request.form['url2']
        key1 = key_words(web1)
        key2 = key_words(web2)
        oran = benzerlik_orani(key1, key2)

    return render_template("benzerlik_skorlamasi.html", oran=oran, key1=key1, key2=key2)


@app.route("/indexleme_siralama", methods=['GET', 'POST'])
def indexleme_siralama():
    ana_url = None
    kume_url = None
    html_text = None
    if request.method == 'POST':
        ana_url = request.form['url']
        kume_url = request.form['urlqueue']
        html_text = indexle_sirala(ana_url, kume_url)
        html_text = html_text.split('\n')
    return render_template("indexleme_siralama.html", html_text=html_text)


@app.route("/semantik_analiz")
def semantik_analiz():
    return render_template("semantik_analiz.html")


if __name__ == "__main__":
    app.run()
