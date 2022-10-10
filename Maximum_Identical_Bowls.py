n=int(input())
a=set(map(int,input().split()))
b=sum(a)
while b%n!=0:
    n-=1
print(n)   