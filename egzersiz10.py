a=0
for sayi in range(10000,100000):
    sayi_str=str(sayi)
    if sayi_str[0]==sayi_str[3] and sayi_str[1]==sayi_str[4]:
        a=a+1
        print(int(sayi_str))
print(a)
    
