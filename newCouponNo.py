import random
couponList=[]

class ValueLessThan4Digits(Exception):
    "Raised when the input value is less than 4 digits"
    pass

class DuplicateValueInList(Exception):
    "Raised when there is a duplicate value in the list"
    pass

def getNewCoupon(couponList):

    randomCount=0
    newCoupon=0
    while True:
        randomCount+=1
        newCoupon=random.randrange(1000,10000)
        if newCoupon not in couponList:
            break
    return newCoupon,randomCount
    

try:
    noOfCoupons=int(input("enter the number of coupons"))
    if noOfCoupons<=0:
        raise ValueError
    else:
        print("enter the coupon numbers(4-digit)")
        for index in range(noOfCoupons):
            couponList.append(int(input()))

        for element in couponList:
            if element<1000 or element>9999:
                raise ValueLessThan4Digits

        for element in couponList:
            duplicateCheckList=couponList.copy()
            duplicateCheckList.remove(element)
            if element in duplicateCheckList:
                raise DuplicateValueInList


except ValueError:
    print("kindly enter only positive integers")

except ValueLessThan4Digits:
    print("kindly enter only 4-Digit positive integers for the coupon numbers")
except DuplicateValueInList:
    print("kindly enter distinct coupon numbers")
else:
    newCoupon,randomCount=getNewCoupon(couponList)
    print("New Coupon : "+str(newCoupon)+"\nNo. of random numbers generated : "+str(randomCount))        