
sayi=input("3 veya 4 basamaklı bir sayı giriniz:")
sayi_str=str(sayi)
if len(sayi_str)==3:
    if sayi_str[0]==sayi_str[2]:
        print("Girdiğiniz sayı 3 basamaklı palindromik bir sayıdır.")
    else:
        print("Girdiğiniz sayı palindromik değildir.")
elif len(sayi_str)==4:
    if sayi_str[0]==sayi_str[3] and sayi_str[1]==sayi_str[2]:
        print("Girdiğiniz sayı 4 basamaklı palindromik bir sayıdır.")
    else:
        print("Girdiğiniz sayı palindromik değildir.")
else:
    print("Lütfen 3 veya 4 basamaklı bir sayı girin.")
