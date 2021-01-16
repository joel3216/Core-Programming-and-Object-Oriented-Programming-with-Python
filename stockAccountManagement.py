import json
from operator import itemgetter
class stockAccountManagement:
    
    def getIndex(self,symbol):
        fileHandle=open("stocks.json","r")
        try:
            keyFound=False
            records=json.load(fileHandle)
            for record in records:
                if record["stockSymbol"]==symbol:
                    keyFound=True
                    return records.index(record)
            if keyFound==False:
                raise TypeError

        except ValueError:
            symbol=0

    def getRecord(self):
        fileHandle=open("stocks.json","r")
        try:
            records=json.load(fileHandle)
            record=records[-1]
            symbol=record["stockSymbol"]
            symbol+=1
        except ValueError:
            symbol=0
        except IndexError:
            symbol=0
        
        try:
            record={}
            record["stockSymbol"]=symbol
            record["stockName"]=input("enter the stock name ")
            record["shares"]=int(input("enter the number of shares "))
            record["price"]=float(input("enter the share price "))
        except ValueError:
            print("please enter valid inputs")
            self.getRecord()
        else:        
            return record

    def add2stocks(self,record):
        fileHandle=open("stocks.json","r")
        try:
            records=json.load(fileHandle)
        except ValueError:
            records=[]
        records.append(record)
        self.updateStocks(records)

    def updateStocks(self,records):
        fileHandle=open("stocks.json","w")
        fileHandle.writelines(json.dumps(records))
        fileHandle.close()

    def stockReport(self):
        fileHandle=open("stocks.json","r")
        stocks=json.load(fileHandle)
        totalValue=0
        for stock in stocks:
            getPrice=itemgetter("price")
            getShares=itemgetter("shares")
            price=getPrice(stock)
            share=getShares(stock)
            value=price*share
            totalValue+=value
            print(stock["stockName"]+" value : "+str(value))
        print("Total Value: "+str(totalValue))

    def buyShares(self):
        try:
            symbol=int(input("enter the stock symbol of the account"))
            index=self.getIndex(symbol)
        except ValueError:
            print("please enter only poitive integers for the symbol")
        except TypeError:
            print("key not found")
        else:
            fileHandle=open("stocks.json","r")
            records=json.load(fileHandle)
            try:
                newShares=int(input("enter the number of shares to buy"))
            except ValueError:
                print("please enter valid inputs")
                self.buyShares
            else:
                records[index]["shares"]+=newShares
                self.updateStocks(records)

    def sellShares(self):
        try:
            symbol=int(input("enter the stock symbol of the account"))
            index=self.getIndex(symbol)
        except ValueError:
            print("please enter only poitive integers for the symbol")
        except TypeError:
            print("key not found")
        else:
            fileHandle=open("stocks.json","r")
            records=json.load(fileHandle)
            try:
                soldShares=int(input("enter the number of shares to sell"))
                if soldShares>records[index]["shares"]:
                    raise ValueError
            except ValueError:
                print("please enter valid inputs")
                self.buyShares
            else:
                records[index]["shares"]-=soldShares
                self.updateStocks(records)


if __name__ == "__main__":
    stockObj= stockAccountManagement()
    while True:
            try:
                choice=int(input("enter 1 to add new account\nenter 2 to print stock report\nenter 3 to buy shares\nenter 4 to sell shares\nenter 5 to sort by name\nenter 6 to sort by zip\nenter 0 to quit "))
                if choice==0:
                    break
                elif choice==1:
                    record=stockObj.getRecord()
                    stockObj.add2stocks(record)
                elif choice==2:
                    stockObj.stockReport()
                elif choice==3:
                    stockObj.buyShares()
                elif choice==4:
                    stockObj.sellShares()
                elif choice==5:
                    pass
                elif choice==6:
                    pass
            except ValueError:
                print("Please choose from the specified options")    