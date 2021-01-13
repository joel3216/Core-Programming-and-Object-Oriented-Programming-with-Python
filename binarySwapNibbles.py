import util

class binarySwapNibbles:
    def fillZeros(self,binary):
        for counter in range(8-len(binary)):
            binary="0"+binary
        return binary

    def isPowerOfTwo(self,number):
        if (number == 0):
            return False
        while (number != 1):
                if (number % 2 != 0):
                    return False
                number = number // 2
                
        return True
    
    def swapNibbles(self,number):
        binary=str(util.util.toBinary(number))
        if len(binary)<8:
            binary=binarySwapNibbles.fillZeros(binarySwapNibbles,binary)
        swapbinary=binary[4:]+binary[:4]
        return swapbinary

    def binary2Decimal(self,binary):
        decimal, power = 0, 0
        while(binary != 0): 
            remainder = binary % 10
            decimal += remainder * (2**power) 
            binary = binary//10
            power += 1
        return decimal  

if __name__ == "__main__":
    
    try:
        number=int(input("enter an integer"))
    except ValueError:
        print("enter integers only")
    else:
        swapbinary=binarySwapNibbles.swapNibbles(binarySwapNibbles,number)
        newDecimal=binarySwapNibbles.binary2Decimal(binarySwapNibbles,int(swapbinary))
        if binarySwapNibbles.isPowerOfTwo(binarySwapNibbles,newDecimal):
            print(str(newDecimal)+" is a power of 2")
        else:
            print(str(newDecimal)+" is not a power of 2")
