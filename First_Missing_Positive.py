n=int(input())
l=list(map(int,input().split()))
k=max(l)
d=[]
for i in range(k*k):
    if i not in l:
        d.append(i)
if(d[0]!=0):
    print(d[0])
else:
    print(d[1])