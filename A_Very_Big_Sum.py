n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in range(len(arr)):
    sum=sum+arr[i]
print(sum)