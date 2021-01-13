class vendingMachine:
        
    def getMinNotes(self,change,notes):
        notesUsed=[]
        noOfNotes=0
        for note in reversed(notes):
            while(change>0):
                if change-note>=0:
                    change-=note
                    noOfNotes+=1
                    notesUsed.append(note)
                else:
                    break
            if change<=0:
                break
        return noOfNotes,notesUsed

    
if __name__ == "__main__":
    try:
        change=int(input("enter the change to be returned"))
        if change<=0:
            raise ValueError
    except ValueError:
        print("please enter a positive integer")
    else:
        notes=[1,2,5,10,50,100,500,1000]
        noOfNotes,notesUsed=vendingMachine.getMinNotes(vendingMachine,change,notes)
        print("No. of notes: "+str(noOfNotes)+"\nNotes returned: "+str(notesUsed))
