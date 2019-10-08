import math

toplam=0

for n in range (1,1000000):
    
    toplam=toplam + 1/pow(n,2)

print(pow(toplam*6,1/2))
