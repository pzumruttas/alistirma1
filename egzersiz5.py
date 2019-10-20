#4 basamaklı palindromik sayilari bastitir

for sayi in range(1000,10000):
    sayi_str=str(sayi)
    if sayi_str[::1]==sayi_str[::-1]:
        print(sayi,end=" ")
