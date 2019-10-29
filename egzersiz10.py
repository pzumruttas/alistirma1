a=0
for sayi in range(10000,100000):
    sayi_str=str(sayi)
    if sayi_str[:2]==sayi_str[3:]:
        a=a+1
    
print(a)
