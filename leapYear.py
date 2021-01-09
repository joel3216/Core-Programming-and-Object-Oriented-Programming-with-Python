def leapYearCheck(year):
    isLeap=False
    if year%400==0:
        isLeap=True
    elif year%100==0:
        isLeap=False
    elif year%4==0:
        isLeap=True
    return isLeap
try:
    year=int(input("enter a four digit year"))
    if year>999:
        isLeap=leapYearCheck(year)
        if bool(isLeap):
            print(str(year)+" is a leap year")
        else:
            print (str(year)+" is not a leap year")
    else:
        print(str(year)+" contains less than 4-digits")
except ValueError:
    print("invalid year, please enter a 4-digit integer")