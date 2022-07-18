d=input()
d=d.lower()
k=input()
k=k.lower()
d=d.split()
k=k.split()
t=[]
for i in k:
    if i in d:
        t.append(i)
print(*t)