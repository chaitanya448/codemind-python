import math
def result(c):
    l=0
    r=int(math.sqrt(c))
    while l<=r:
        summ=l*l+r*r
        if summ ==c:
            return True
        if summ <c:
            l+=1
        else:
            r-=1
    return False 
a=int(input())
print(result(a))