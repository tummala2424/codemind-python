x=int(input())
c=0
for i in range(x+1):
    for j in range(x+1):
        if(i*i+j*j==x and i!=j):
            c+=1
            print("True")
            break
    if(c>0):
        break
if c==0:
    print("False")