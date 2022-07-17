n=int(input())
k=list(map(int,input().split()))
d,b=map(int,input().split())
c=0
min=999
for i in range(n):
    if k[i]>=d and k[i]<=b:
        c=1
        if k[i]<min:
            min=k[i]
if c==0:
    print(-1)
else:
    print(min)