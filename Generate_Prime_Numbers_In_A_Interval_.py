def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(i==1):
        continue
    if prime(i):
        print(i,end='
')