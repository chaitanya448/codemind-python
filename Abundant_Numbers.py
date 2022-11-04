n=int(input())
m=0
x=[]
for i in range(1,n):
    if n%i==0:
       x.append(i)
for i in x:
    m=m+i
if m>n:
    print(True)
else:
    print(False)