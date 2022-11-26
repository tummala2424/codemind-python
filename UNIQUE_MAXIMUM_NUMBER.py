n=int(input())
arr=list(map(int,input().split()))
c=0
max=0
s=0
for i in range(len(arr)):
    c=0
    for j in range(len(arr)):
        if i!=j:
            if arr[i]==arr[j]:
                c+=1
    if c==0 and arr[i]>max:
        max=arr[i]
        s+=1
if s>0:
    print(max)
else:
    print("-1")