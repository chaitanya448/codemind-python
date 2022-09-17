x=int(input())
t=x
p=1
s=0
while x>0:
    r=x%10
    p=p*r
    s=s+r
    x=x//10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")