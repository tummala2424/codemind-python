s=input()
d=len(s)
t=input()
k=0
for i in range(0,d):
    if(s[i]==t):
        k+=1
if(k==0):
    print('-1')
else:
    print(k)