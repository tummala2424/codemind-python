n=input()
n=n.lower()
n=n.split()
a='aeiou'
c=0
for i in n:
    if i[0] in a and i[len(i)-1] not in a:
        c+=1
print(c)