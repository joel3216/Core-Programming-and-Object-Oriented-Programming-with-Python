from itertools import permutations
import random
couponList=[]

class DuplicateValueInList(Exception):
    "Raised when there is a duplicate value in the list"
    pass

def getPermutations(couponList):
    couponPermutations=[]
    permutationList=list(permutations(couponList))
    for permutation in permutationList:
        extractedNumber=""
        for element in permutation:
            extractedNumber+=str(element)
        couponPermutations.append(int(extractedNumber))
    return couponPermutations

def getRandomCount(couponPermutations):

    randomCount=0    
    while len(couponPermutations)>0:
        randomCount+=1
        newCoupon=random.randrange(max(couponPermutations)+1)
        if newCoupon in couponPermutations:
            couponPermutations.remove(newCoupon)

    return randomCount
    

try:
    noOfCoupons=int(input("enter the number of coupons"))
    if noOfCoupons<=0:
        raise ValueError
    else:
        print("enter the coupon numbers")
        for index in range(noOfCoupons):
            couponList.append(int(input()))

        for element in couponList:
            duplicateCheckList=couponList.copy()
            duplicateCheckList.remove(element)
            if element in duplicateCheckList:
                raise DuplicateValueInList


except ValueError:
    print("kindly enter only positive integers")
except DuplicateValueInList:
    print("kindly enter distinct coupon numbers")
else:
    couponPermutations=getPermutations(couponList)
    randomCount=getRandomCount(couponPermutations)
    print("No. of random numbers generated : "+str(randomCount))