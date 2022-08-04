d=input()
k=[]
for i in d:
    if i in '.':
        k.append('[')
        k.append(i)
        k.append(']')
    else:
        k.append(i)
for i in k:
    print(i,end='')