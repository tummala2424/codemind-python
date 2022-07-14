n=int(input())
arr=list(map(int,input().split()))
k=int(n/2)
for i in range(n-1,k-1,-1):
    print(arr[i],end=' ')
for i in range(0,k):
    print(arr[i],end=' ')