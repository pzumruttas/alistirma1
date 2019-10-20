#ilk rakamı son rakamından büyük olan 4 basamaklı sayı adedini verir.
sayac=0
for sayi in range(1000,10000):
    sayi_str=str(sayi)
    if sayi_str[0]>sayi_str[3]:
        sayac=sayac+1

print(sayac)
