import math

a = 0
for x in range(1,125):
    K1 = 125%x
    K2 = 200%x
    K3 = 350%x
    if K1==K2 and K2==K3 and K1==K3 and K1!=0:
        K=K1
        if a<K:
            a=K
            x_max=x
print(x_max)
