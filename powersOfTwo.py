def printPowerTableOf2(n):
    for i in range(n):
        print("2^"+str(i)+": "+str(2**i))

try:
    n=int(input("enter the maximum power of 2 "))
    if(n>0):
        printPowerTableOf2(n)
    else:
        raise ValueError
except ValueError:
    print("please enter a positive integer")