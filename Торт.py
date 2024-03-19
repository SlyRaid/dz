##x=int(input())
##
##if x!=0:
##    if x>2:
##        print(x/2)
##    else:
##        print(x-1)
##else:
##    print(0)

n=int(input('Число гостей? '))
if n<2: n=0
print (int(n/2) if n%2==0 else n)
