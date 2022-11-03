def is_prime(p):
    if p%2==0:
        return False
    else:
        for i in range(3,p,2):
            if p%i==0:
                return False
    return True
a=int(input())
b=is_prime(a)
a=str(a)
c=int(a[::-1])
d=is_prime(c)
if b==True and d==True:
    print('circular prime')
elif b==True and d==False:
    print('prime but not a circular prime')
else:
    print('not prime')