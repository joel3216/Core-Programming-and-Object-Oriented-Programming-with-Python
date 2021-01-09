integerList=[]

def getZeroSumTriplets(integerList):
    zeroSumTriplets=[]
    for index1 in range(len(integerList)-2):
        for index2 in range(index1+1,len(integerList)-1):
            for index3 in range(index2+1,len(integerList)):
                if integerList[index1]+integerList[index2]+integerList[index3]==0:
                    zeroSumTriplets.append(str(integerList[index1])+","+str(integerList[index2])+","+str(integerList[index3]))
                    break
    return zeroSumTriplets
try:
    listSize=int(input("enter the number of elements"))
    print("enter the elements")

    for index in range(listSize):
        integerList.append(int(input()))

    zeroSumTriplets=getZeroSumTriplets(integerList)
    print(zeroSumTriplets)

except ValueError:
    print("Kindly enter integers only")
        
