
kelimeler = None
kelimesozluk = dict()
with open("esanlamlikelimeler.txt") as f:
    kelimeler = f.readlines()
for kelime in kelimeler:
    kelime1,kelime2 = kelime.split(",")
    kelimesozluk[kelime1] = kelime2
    kelimesozluk[kelime2] = kelime1
print(kelimesozluk.get("çok"))
