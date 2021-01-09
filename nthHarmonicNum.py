def getHarmonicValue(limit):
    harmonicSum=0
    for number in range(1,limit+1):
        harmonicSum+=(1/number)

    print(str(limit)+"th Harmonic value is "+str(harmonicSum))

try:
    limit=int(input("enter the maximum limit for harmonic numbers"))

    if limit>0:
        getHarmonicValue(limit)
    else:
        raise ValueError
except ValueError:
    print("please enter a positive integer")