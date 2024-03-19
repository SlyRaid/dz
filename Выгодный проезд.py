n, m, a, b = map(int, input().split())
e = (n % m * a) + (n // m * b) #абонементы + билеты
f = ((n // m + 1) * b) #если выгодно больше абонементов
g = n * a #если выгодно только билеты
if e > f:
    print(int(f))
elif g < e and g < f:
    print(int(g))
else:
    print(int(e))
