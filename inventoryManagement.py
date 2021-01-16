import json
from operator import itemgetter

class inventoryManagement:
    def inventoryFactory(self,fileHandle):
        inventory=json.load(fileHandle)
        return inventory        
    
    def calculateValue(self,inventory):
        totalValue=0
        for item in inventory:
            getValue=itemgetter("value")
            getWeight=itemgetter("weight")
            itemValue=getValue(inventory[item])
            itemWeight=getWeight(inventory[item])
            itemValue*=itemWeight
            totalValue+=itemValue
            print(item+" value:"+str(itemValue))
        print("Total value:"+str(totalValue))

if __name__ == "__main__":
        
    fileHandle=open("inventory.json","r")
    inventoryObj=inventoryManagement()
    inventory=inventoryObj.inventoryFactory(fileHandle)
    inventoryObj.calculateValue(inventory)
    fileHandle.close()