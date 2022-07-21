s=input()
a=len(s)
x=0
for i in range(0,a):
    if(s[i]>='0' and s[i]<='9'):
        x+=1
if(x!=0):
    print('Contains',x,'digit')
else:
    print("Doesn't contain digit")