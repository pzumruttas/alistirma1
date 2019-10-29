toplam=0

for yil in range(1000,2005):
    str_yil=str(yil)
    for i in range(1,5):
        toplam=toplam+int(str_yil[i-1])
    if (2005-yil)==toplam:
        print(yil)
    toplam=0
