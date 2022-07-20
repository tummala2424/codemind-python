t=int(input())
for i in range(t):
    a=int(input())
    for j in range(1,a+1):
        k=j*j
        if a==k:
            print('True')
            break
    else:
        print('False')