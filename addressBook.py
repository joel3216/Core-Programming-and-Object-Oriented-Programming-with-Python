import json
from operator import itemgetter
class addressBook:
    def getRecord(self):
        fileHandle=open("addressBook.json","r")
        try:
            records=json.load(fileHandle)
            record=records[-1]
            uid=record["uniqueID"]
            uid+=1
        except ValueError:
            uid=0
        except IndexError:
            uid=0
        
        record={}
        record["uniqueID"]=uid
        record["firstname"]=input("enter the firstname ")
        record["lastname"]=input("enter the lastname ")
        record["address"]=input("enter the address ")
        record["city"]=input("enter the city ")
        record["state"]=input("enter the state ")
        record["zip"]=input("enter the zipcode ")
        record["phone"]=input("enter the phone no. ")
        return record

    def getIndex(self,uid):
        fileHandle=open("addressBook.json","r")
        try:
            keyFound=False
            records=json.load(fileHandle)
            for record in records:
                if record["uniqueID"]==uid:
                    keyFound=True
                    return records.index(record)
            if keyFound==False:
                raise TypeError

        except ValueError:
            uid=0

    def add2addressBook(self,record):
        fileHandle=open("addressBook.json","r")
        try:
            records=json.load(fileHandle)
        except ValueError:
            records=[]
        records.append(record)
        self.updateAddressBook(records)
    
    def updateAddressBook(self,records):
        fileHandle=open("addressBook.json","w")
        fileHandle.writelines(json.dumps(records))
        fileHandle.close()

    def readAddressBook(self):
        fileHandle=open("addressBook.json","r")
        try:
            records=json.load(fileHandle)
            if len(records)==0:
                raise ValueError
        except ValueError:
            print("Address book is empty!")
        else:
            for record in records:
                print(str(record)+"\n")
    
    def deleteRecord(self):
        try:
            uid=int(input("enter the unique key of the record you want to delete"))
            index=self.getIndex(uid)
        except ValueError:
            print("please enter only poitive integers for the index")
        except TypeError:
            print("key not found")
        else:
            fileHandle=open("addressBook.json","r")
            records=json.load(fileHandle)
            records.pop(index)
            self.updateAddressBook(records)
    
    def editRecord(self):
        try:
            uid=int(input("enter the unique key of the record you want to edit"))
            index=self.getIndex(uid)
        except ValueError:
            print("please enter only poitive integers for the index")
        except TypeError:
            print("key not found")
        else:
            fileHandle=open("addressBook.json","r")
            records=json.load(fileHandle)
            for key in records[index].keys():
                if key=="uniqueID":
                    continue
                choice=input("update "+str(key)+" ? (y/n)")
                if choice=='y':
                    records[index][key]=input("enter the "+str(key))

            self.updateAddressBook(records)

    def sortByName(self):
        fileHandle=open("addressBook.json","r")
        records=json.load(fileHandle)
        records.sort(key=itemgetter("firstname"))
        self.updateAddressBook(records)
    
    def sortByZip(self):
        fileHandle=open("addressBook.json","r")
        records=json.load(fileHandle)
        records.sort(key=itemgetter("zip"))
        self.updateAddressBook(records)

if __name__ == "__main__":
    addressBookObj=addressBook()

    while True:
        try:
            choice=int(input("enter 1 to add new record\nenter 2 to print address book\nenter 3 to delete a record\nenter 4 to edit a record\nenter 5 to sort by name\nenter 6 to sort by zip\nenter 0 to quit "))
            if choice==0:
                break
            elif choice==1:
                record=addressBookObj.getRecord()
                addressBookObj.add2addressBook(record)
            elif choice==2:
                addressBookObj.readAddressBook()
            elif choice==3:
                addressBookObj.deleteRecord()
            elif choice==4:
                addressBookObj.editRecord()
            elif choice==5:
                addressBookObj.sortByName()
            elif choice==6:
                addressBookObj.sortByZip()
        except ValueError:
            print("Please choose from the specified options")    