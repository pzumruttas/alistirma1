toplam=0

for sayi in range(1,1000):
    str_sayi=str(sayi)
    for i in range(0,len(str_sayi)):
        toplam=toplam+int(str_sayi[i])
    if toplam<9:
        print(sayi, end=" ")
    toplam=0
