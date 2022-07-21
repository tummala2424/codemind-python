t=input()
l=len(t)
v=0
c=0
d=0
s=0
for i in range(0,l):
    if(t[i]>='0' and t[i]<='9'):
        d+=1
    elif(t[i]==' '):
        s+=1
    elif(t[i]=='a' or t[i]=='e' or t[i]=='i' or t[i]=='o' or t[i]=='u'):
        v+=1
    else:
        c+=1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',s)