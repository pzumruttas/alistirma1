toplam=0

for sayi in range(1,1000):
    str_sayi=str(sayi)
    for i in range(1,len(str_sayi)+1):
        toplam=toplam+int(str_sayi[i-1])
    if toplam<9:
        print(sayi, end=" ")
    toplam=0
