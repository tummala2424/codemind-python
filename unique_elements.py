n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(n):
    if a[i] not in c:
        c.append(a[i])
print(*c)