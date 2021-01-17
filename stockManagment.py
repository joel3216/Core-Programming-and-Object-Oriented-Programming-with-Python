from datetime import datetime
class transactionNode():
    def __init__(self,transactionType,symbol,shares):
        now=datetime.now()
        self.transactionType=transactionType
        self.symbol=symbol
        self.shares=shares
        self.dateTime=now.strftime("%d/%m/%Y %H:%M:%S")
        self.next=None

class stockNode():
    def __init__(self,account):
        self.symbol=account["stockSymbol"]
        self.stockName=account["stockName"]
        self.shares=account["shares"]
        self.price=account["price"]
        self.next=None

class linkedStocks():
    def __init__(self):
        self.stockHead=None
        self.transactionHead=None

    def addNextTransactionNode(self,transactionType,symbol,shares):
        temp=self.transactionHead
        if(not temp):
            self.transactionHead=transactionNode(transactionType,symbol,shares)
        else:
            while(temp):
                if(not temp.next):
                    temp.next=transactionNode(transactionType,symbol,shares)
                    break
                temp=temp.next

    def addNextStockNode(self,account):
        temp=self.stockHead
        if(not temp):
            self.stockHead=stockNode(account)
        else:
            while(temp):
                if(not temp.next):
                    temp.next=stockNode(account)
                    break
                temp=temp.next
    
    def distinctSymbolCheck(self,symbol):
        temp=self.stockHead
        while(temp):
            if temp.symbol==symbol:
                print("this symbol already exists, please enter another or update this account")
                return False
            else:
                temp=temp.next
        return True

    def printTransactionLinkedList(self):
        temp=self.transactionHead
        if(not temp):
            print("Linked List is empty!")
        else:
            while(temp):
                print("\nTransaction Type: "+temp.transactionType+"\nStock Symbol: "+temp.symbol+"\nShares Transferred: "+str(temp.shares)+"\nDate & Time: "+temp.dateTime+"\n")
                temp=temp.next
            
    def printStockLinkedList(self):
        temp=self.stockHead
        if(not temp):
            print("Linked List is empty!")
        else:
            while(temp):
                print("\nStock Symbol: "+temp.symbol+"\nStock Name: "+temp.stockName+"\nNo. of Shares"+str(temp.shares)+"\nPrice: "+str(temp.price)+"\n")
                temp=temp.next
    
    def getStockAccount(self):
        try:
            account={}
            account["stockSymbol"]=input("enter the stock symbol")
            if not self.distinctSymbolCheck(account["stockSymbol"]):
                raise ValueError
                
        except ValueError:
            print("please enter valid inputs")
            self.getStockAccount()
        else:
            account["stockName"]=input("enter the stock name ")
            account["shares"]=int(input("enter the number of shares "))
            account["price"]=float(input("enter the share price "))        
            self.addNextStockNode(account)
    
    def buyShares(self):
        symbol=input("enter the stock symbol")
        temp=self.stockHead
        while(temp):
            if temp.symbol==symbol:
                try:
                    newShares=int(input("enter the number of shares to buy"))
                    if newShares<0:
                        raise ValueError
                except ValueError:
                    print("ERROR: Number of shares cannont be negative")
                else:
                    temp.shares+=newShares
                    self.addNextTransactionNode("purchase",temp.symbol,newShares)
                    break
            temp=temp.next
    
    def sellShares(self):
        symbol=input("enter the stock symbol")
        temp=self.stockHead
        while(temp):
            if temp.symbol==symbol:
                try:
                    soldShares=int(input("enter the number of shares to sell"))
                    if soldShares<0:
                        raise ValueError
                    if soldShares>temp.shares:
                        raise ValueError
                except ValueError:
                    print("ERROR: Number of shares cannont be negative or greater than shares available")
                else:
                    temp.shares-=soldShares
                    self.addNextTransactionNode("sale",temp.symbol,soldShares)
                    break
            temp=temp.next        

if __name__ == "__main__":
    linkedList=linkedStocks()
    while True:
            try:
                choice=int(input("enter 1 to add new account\nenter 2 to print stock report\nenter 3 to buy shares\nenter 4 to sell shares\nenter 5 to print transaction history\nenter 0 to quit "))
                if choice==0:
                    break
                elif choice==1:
                    linkedList.getStockAccount()
                    
                elif choice==2:
                    linkedList.printStockLinkedList()
                elif choice==3:
                    linkedList.buyShares()
                elif choice==4:
                    linkedList.sellShares()
                elif choice==5:
                    linkedList.printTransactionLinkedList()
            except ValueError:
                print("Please choose from the specified options")        