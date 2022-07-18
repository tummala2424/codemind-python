n=input()
a=999
b=999
for i in n:
    if ord(i)>=97:
        if a>ord(i):
            a=ord(i)
    if b>ord(i):
        b=ord(i)
if abs(a-97)<=abs(b-65):
    print(chr(a))
else:
    print(chr(b))