n,m=map(int,input().split())
c=0
for i in range(1,m+1):
    if n%i==0  and m%i==0: 
        c=i
print(c)