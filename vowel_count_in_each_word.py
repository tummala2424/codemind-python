s=input()
n=s.split()
for word in n:
    count=0
    for ch in word:
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
            count=count+1
    print(count,end=" ")