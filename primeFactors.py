num=int(input("enter the number to compute its prime factors"))

i=2
factors=[]
while i<=num:
    if num%i==0:
        factors.append(i)
        num/=i
    else:
        i+=1

print(factors)