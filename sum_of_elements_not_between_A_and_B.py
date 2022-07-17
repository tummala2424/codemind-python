n=int(input())
a=list(map(int,input().split()))
c,d=map(int,input().split())
s=0
for i in range(n):
    if a[i]<c or a[i]>d:
        s=s+a[i]
print(s)