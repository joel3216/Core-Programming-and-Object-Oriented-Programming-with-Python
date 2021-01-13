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
        return round(payment,2)
    
    @staticmethod
    def dayOfWeek(d,m,y):
        days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        months=["January","February","March","April","May","June","July","August","September","October","November","December"]
        y0=int( y - (14 - m) / 12 )
        x=int( y0 + y0/4 - y0/100 + y0/400 )
        m0=int( m + 12 * ((14 - m) / 12) - 2 )
        d0=int( (d + x + (31*m0)/12) % 7 )
        print(d0)

        return days[d0],months[m-1]
    
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