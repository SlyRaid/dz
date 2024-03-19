a=int(input())
b=int(input())
n=int(input())

a=n*a+n*b//100 #рубли
b=n*b%100      #копейки
print(a,b)
