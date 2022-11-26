n=int(input())
arr=list(map(int,input().split()))
c=0
m=[]
for i in range(len(arr)):
    if(arr[i]==1):
        c+=1
    else:
        m.append(c)
        c=0
m.append(c)
print(max(m))
