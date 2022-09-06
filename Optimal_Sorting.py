t=int(input())
for i in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    d=sorted(li)
    if li==d:
        print('0')
        break
    else:
       k=d[-1]-d[0]
       print(k)