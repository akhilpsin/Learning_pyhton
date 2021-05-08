class hospital:
    def __init__(self,dname,aname,nname,ddept,adept,ndept):
        self.dname=dname
        self.aname=aname
        self.nname=nname
        self.ddept=ddept
        self.adept=adept
        self.ndept=ndept
    def getnames(self):
        self.dname=input("Please provide doctor name: ")
        self.ddept=input("Please provide doctor departmnet: ")
        self.aname=input("Please provide admin name: ")
        self.adept=input("Please provide admin departmnet: ")
        self.nname=input("Please provide sister name: ")
        self.ndept=input("Please provide sister departmnet: ")

class department(hospital):
    def display(self):
        print('doctor ',self.dname,' is in department ',self.ddept)
        print('admin ',self.aname,' is in department ',self.adept)
        print('sister ',self.nname,' is in department ',self.ndept)

class patientward(department):
    def __init__(pself,pname,page,pno,pdes):
        pself.pname=pname
        pself.page=page
        pself.pno=pno
        pself.pdes=pdes
    def getpnames(pself):
        pself.pname=input("Please provide patient name: ")
        pself.page=input("Please provide patient age: ")
        pself.pno=input("Please provide patient no: ")
        pself.pdes=input("Please provide desease details: ")
    def printoutp(pself):
        print('patient name: ',pself.pname)
        print('patient age:  ',pself.page)
        print('patient number:  ',pself.pno)
        print('patient desease info:  ',pself.pdes)

obbj=patientward('','','','')
obbj.getpnames()
obbj.getnames()
obbj.display()
obbj.printoutp()
