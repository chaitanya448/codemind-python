n=int(input())
c=str(n)
if n<0:
    c=c[1:]
    c=c[::-1]
    print(0-int(c))
else:
    print(int(c[::-1]))