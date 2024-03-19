import math
a=int(input())
b=int(input())
c=int(input())

#math.ceil для округления вверх
k1=math.ceil(a/2) #кол-во парт 1 класс
k2=math.ceil(b/2) #кол-во парт 2 класс
k3=math.ceil(c/2) #кол-во парт 3 класс

print(k1+k2+k3)
