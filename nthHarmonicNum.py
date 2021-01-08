n=int(input("enter the maximum limit for harmonic numbers"))
harmonicSum=0

if n>0:
    for i in range(1,n+1):
        harmonicSum+=(1/i)

    print(str(n)+"th Harmonic value is "+str(harmonicSum))
    print(i)
else:
    print("invalid input")