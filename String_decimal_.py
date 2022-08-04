t=int(input())
c=0
for i in range(t):
    s=input()
    for i in s:
        if i in "1234567890":
            c+=1
    if len(s)==c:
        print('True')
    else:
        print('False')
    c=0