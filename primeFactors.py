def getPrimeFactors(num):
    i=2
    factors=[]
    while i<=num:
        if num%i==0:
            factors.append(i)
            num/=i
        else:
            i+=1

    return factors

try:
    num=int(input("enter the number to compute its prime factors"))
    if num>0:
        print(getPrimeFactors(num))
    else:
        raise ValueError
except ValueError:
    print("please enter a positive integer")