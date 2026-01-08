n = int(input())

grn = n // 100
kop = n % 100

if kop == 0:
    print(grn)
else:
    print(grn, kop)