t=int(input())
for i in range (t):
    n=int(input())
    l=list(map(int,input().split()))
    s=[]
    for i in l:
        s.append(i)
    s.sort()
    if(s==l):
        print(0)
    else:
        print(max(l)-min(l))