a=int(input())
x=a*a
sum1=0
while x>0:
    ne=x%10
    x=x//10
    sum1+=ne
if a==sum1:
    print("Neon Number")
else:
    print("Not Neon Number")
