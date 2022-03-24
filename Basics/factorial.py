#recursion method
n=int(input("enter number:"))

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(n))

#single line
def fact(n):
    return 1 if n==1 or n==0 else n*fact(n-1)

#iterative method
n=int(input("enter number:"))
res=1
while(n>1):
    res=res*n
    n=n-1
print(res)

#using inbuilt method
import math
n=int(input("enter num:"))
print(math.factorial(n))


