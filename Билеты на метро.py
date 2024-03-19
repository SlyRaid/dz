n = int(input())

a = n % 60

if a >= 35:
    t = n // 60 + 1
    n = 0
    m = 0
else:
    t = n // 60
    if (a % 10) >= 9:
        n = a // 10 + 1
        m = 0
    else:
        n = a // 10
        m = a % 10

print(m, n ,t)
