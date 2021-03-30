
def benzerlik_orani(key1, key2):
    try:
        benzer_sayi = 0
        farkli_sayi = 0
        toplam_sayi = len(key1)
        kelime_benzerlik_orani = 0
        katsayi_benzerlik_orani = 0
        benzerlik_oran = 0
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
