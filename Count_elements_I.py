x,y=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
l=set(l)
m=set(m)
c=0
for i in l:
    if i in m:
        c+=1
print(c)
