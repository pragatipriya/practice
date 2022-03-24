n=input("Enter number:")
order=len(n)
sum=0
num=int(n)
temp=num

while(temp>0):
    digit=temp%10
    sum+=digit**order
    temp=temp//10

if num==sum:
    print("armstrong")
else:
    print("Not armstrong")