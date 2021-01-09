year=int(input("enter a four digit year"))
leap=False
if year>999:
    if year%400==0:
        leap=True
    elif year%100==0:
        leap=False
    elif year%4==0:
        leap=True

    if bool(leap):
        print(str(year)+" is a leap year")
    else:
        print (str(year)+" is not a leap year")
else:
    print(str(year)+" contains less than 4-digits")