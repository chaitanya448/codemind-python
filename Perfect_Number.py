n=int(input())
su1=0
for i in range (1,n):
    if (n%i==0):
        su1+=i
if (su1==n):
    print(True)
else:
    print(False)