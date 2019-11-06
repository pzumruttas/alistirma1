#1. ve 2. basamaktaki rakamları toplamı 3. basamktakine eşit olan 3 basamaklı sayıların sayısını ve kendilerini bastırır
sayac=0
for sayi in range(100,1000):
    sayi_str=str(sayi)
    if int(sayi_str[0])+int(sayi_str[1])==int(sayi_str[2]):
        sayac=sayac+1
        print(sayi,end=" ")

print(sayac)
