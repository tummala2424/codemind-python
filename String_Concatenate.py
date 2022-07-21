a=input()
b=input()
c=a+b
d=[]
for i in c:
    d.append(ord(i))
d=sorted(d)
for i in d:
    print(chr(i),end='')