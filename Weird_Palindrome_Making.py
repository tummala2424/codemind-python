t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    c=0
    for i in arr:
        if i%2:
            c+=1
    print(c//2)