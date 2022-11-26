n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    arr[i]=arr[i]*arr[i]
arr.sort()
n=len(arr)
for i in range(n):
    print(arr[i],end=" ")

