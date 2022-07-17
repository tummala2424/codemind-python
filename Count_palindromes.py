n=int(input())
a=list(map(int,input().split()))
c=0
r=0
for i in a:
    k=i
    r=0
    while(k):
        d=k%10
        k=k//10
        r=r*10+d
    if r==i:
        c+=1
print(c)