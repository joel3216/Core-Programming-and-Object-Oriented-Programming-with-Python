class util:
    @staticmethod
    def temperatureConversion(temperature,unit):
        if unit=="fahrenheit":
            return (temperature-32)*(5/9)
        else:
            return (temperature*9/5)+32

    @staticmethod
    def monthlyPayment(principalLoan,years,rate):
        
        ratePerPeriod= rate/(12*100)
        periods=12*years

        payment=(principalLoan*ratePerPeriod)/(1-(1+ratePerPeriod)**(-periods))
        return payment
    
    @staticmethod
    def dayOfWeek(day,month,year):
        days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        months=["January","February","March","April","May","June","July","August","September","October","November","December"]
        year0=year-(14-month)/12
        x=year0+year0/4-year0/100+year0/400
        month0=month+12*((14-month)/12)-2
        day0=(day+x+31*month0/12)%7
        print(day0)

        return days[round(day0)],months[int(month)-1]
    
    @staticmethod
    def sqrt(constant):
        t=constant
        epsilon=1e-15
        while abs(t-constant/t)>epsilon*t:
            t=(t+constant/t)/2
        return t

    @staticmethod
    def toBinary(number):
        binaryList=[]
        binary=""
        power=0
        while 2**power<=number:
            binaryList.append(2**power)
            power+=1

        for element in reversed(binaryList):
            if number<element:
                binary+="0"
            else:
                number-=element
                binary+="1"

        return int(binary)