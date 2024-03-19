a,b = input().split()
a = int(a)
b = int(b)

if a > b:
    x = b
else:
    x = a
z = (a + b) - x * 2
c = z // 2
print(x, c)
