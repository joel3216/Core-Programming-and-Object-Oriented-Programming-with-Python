import json

class cliniqueManagement:
    def searchDrByName(self):
        name=input("enter the name of the doctor")
        fileHandle=open("doctors.json","r")
        doctors=json.load(fileHandle)
        keyFound=False
        try:
            print(name+str(doctors[name]))
        except KeyError:
            print("ERROR: Unable to find that doctor!")
        else:
            keyFound=True
        finally:
            fileHandle.close()
            return keyFound,name

    def searchDrBySpecialization(self):
        specialization=input("enter the specialization to search")
        fileHandle=open("doctors.json","r")
        doctors=json.load(fileHandle)
        keyFound=False
        for key in doctors:
            if doctors[key]["specialization"] == specialization:
                keyFound=True
                print(key+str(doctors[key]))
                break
        if keyFound==False:
            print("ERROR: unable to find a doctor specializing in "+specialization)
        else:
            return keyFound,key
    
    def searchDrById(self):
        try:
            searchId=int(input("enter the ID to search"))
        except ValueError:
            print("ERROR: Invalid ID")
        else:
            fileHandle=open("doctors.json","r")
            doctors=json.load(fileHandle)
            keyFound=False
            for key in doctors:
                if doctors[key]["id"] == searchId:
                    keyFound=True
                    print(key+str(doctors[key]))
                    break
            if keyFound==False:
                print("ERROR: unable to find a doctor with id: "+searchId)
            fileHandle.close()
            return keyFound,key

    def searchDrByAvailability(self):
        try:
            searchAvailability=float(input("enter the time when you wish to visit"))
            if searchAvailability<0 or searchAvailability>24:
                raise ValueError
        except ValueError:
            print("ERROR: Invalid time")
        else:
            fileHandle=open("doctors.json","r")
            doctors=json.load(fileHandle)
            keyFound=False
            for key in doctors:
                if doctors[key]["availability"][0] <= searchAvailability and doctors[key]["availability"][1] >= searchAvailability:
                    keyFound=True
                    print(key+str(doctors[key]))
                    break
            if keyFound==False:
                print("ERROR: unable to find a doctor who is available at: "+searchAvailability)
            fileHandle.close()
            return keyFound,key
    
    def searchPatientByName(self):
        name=input("enter the name of the patient")
        fileHandle=open("patients.json","r")
        patient=json.load(fileHandle)
        keyFound=False
        try:
            print(name+str(patient[name]))
            keyFound=True
        except KeyError:
            print("ERROR: Unable to find that patient!")
        finally:
            fileHandle.close()
            return keyFound,name
    
    def searchPatientById(self):
        try:
            searchId=int(input("enter the ID to search"))
        except ValueError:
            print("ERROR: Invalid ID")
        else:
            fileHandle=open("patients.json","r")
            patients=json.load(fileHandle)
            keyFound=False
            for key in patients:
                if patients[key]["id"] == searchId:
                    keyFound=True
                    print(key+str(patients[key]))
                    break
            if keyFound==False:
                print("ERROR: unable to find a patient with id: "+searchId)
            fileHandle.close()
            return keyFound,key
    
    def searchPatientByPhone(self):
        try:
            searchPhone=int(input("enter the phone no. to search"))
        except ValueError:
            print("ERROR: Invalid Phone No.")
        else:
            fileHandle=open("patients.json","r")
            patients=json.load(fileHandle)
            keyFound=False
            for key in patients:
                if patients[key]["phone"] == searchPhone:
                    keyFound=True
                    print(key+str(patients[key]))
                    break
            if keyFound==False:
                print("ERROR: unable to find a patient with phone no: "+searchPhone)
            fileHandle.close()
            return keyFound,key
    
    def searchPatient(self):
        try:
            choice=int(input("enter 5 to search patient by name\nent er 6 to search patient by id\nenter 7 to search patient by phone\nenter 8 to book an appointment\nenter 0 to quit "))
            if choice==5:
                keyFound,patientKey=self.searchPatientByName()
            elif choice==6:
                keyFound,patientKey=self.searchPatientById()
            elif choice==7:
                keyFound,patientKey=self.searchPatientByPhone()
        except ValueError:
                print("Please choose from the specified options")
        else:
            return keyFound,patientKey
    
    def updatePatientList(self,patientList,keyFound,drName):
        patientFile=open("patients.json","r")
        patients=json.load(patientFile)
        if keyFound:
            date=input("enter the date to book an appointment with "+str(drName))
            try:
                patientList[drName+date]
            except KeyError:
                patientList[drName+date]=0

            if patientList[drName+date]<5:
                keyFound,patientKey=self.searchPatient()
                if keyFound:
                    patientList[drName+date]+=1
                    patientList[drName].append(patientKey+str(patients[patientKey])+" Date: "+date)
            else:
                print(drName+" is fully booked, please choose another date")
        return patientList
    
    def bookappointment(self,patientList):
        
        doctorFile=open("doctors.json","r")
        doctors=json.load(doctorFile)
        
        for key in doctors.keys():
            patientList[key]=[]
        while True:
            try:
                choice=int(input("enter 1 to search for a doctor by name\nenter 2 to search for a doctor by speciality\nenter 3 to search for a doctor by their ID\nenter 4 to search for a doctor by availability\nenter 5 to print doctor-patient report\nenter 0 to quit "))
                if choice==0:
                    break
                elif choice==1:
                    keyFound,drName=self.searchDrByName()
                    patientList=self.updatePatientList(patientList,keyFound,drName)

                elif choice==2:
                    keyFound,drName=self.searchDrBySpecialization()
                    patientList=self.updatePatientList(patientList,keyFound,drName)

                elif choice==3:
                    keyFound,drName=self.searchDrById()
                    patientList=self.updatePatientList(patientList,keyFound,drName)

                elif choice==4:
                    keyFound,drName=self.searchDrByAvailability()
                    patientList=self.updatePatientList(patientList,keyFound,drName)

                elif choice==5:
                    print(patientList)
                
            except ValueError:
                print("Please choose from the specified options")

        return patientList



if __name__ == "__main__":
    patientList={}
    clinicObj=cliniqueManagement()
    patientList=clinicObj.bookappointment(patientList)