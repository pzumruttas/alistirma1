toplam=0

for yil in range(1000,2005):
    str_yil=str(yil)
    for i in range(0,4):
        toplam=toplam+int(str_yil[i])
    if (2005-yil)==toplam:
        print(yil)
    toplam=0
