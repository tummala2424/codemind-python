n=input()
c=0
d=0
for i in n:
    c=0
    for j in n:
        if i==j:
            c+=1
    if c>1:
        d+=1
if d==0:
    print("True")
else:
    print("False")