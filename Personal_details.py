class PrsnlDtel :
    def __init__ (self,Name=None,DOJ=None,MobileNo=None,Address=None,Gender=None):
        self.Name = Name
        self.DOJ = DOJ
        self.MobileNo = MobileNo
        self.Address = Address
        self.Gender = Gender 

    def __str__ (self):
        data = str(self.Name)+","+str(self.Gender)+","+str(self.DOJ)+","+str(self.MobileNo)+","+str(self.Address)+","
        return data

    def displayrecord (self):
        print("********************************")
        print("Library Card No : ",self.CardNo)
        print("Name : ",self.Name)
        print("Branch : ",self.Branch)
        print("Date of Join : ",self.DOJ)
        print("Mobile Number : ",self.MobileNo)
        print("Address : ",self.Address)
        print("Gender : ",self.Gender)


if (__name__ == "__main__"):
    CardNo = 10000
    Name = input("Enter Name Here : ")
    Branch = input("Enter Branch Here : ")
    DOJ = input("Enter Date of join Here : ")
    MobileNo = input("Enter a Mobile Number Here : ")
    Address = input("Enter a Address Here : ")
    Gender = input("Enter a Address Here : ")
    dtel = PrsnlDtel(CardNo,Name,Branch,DOJ,MobileNo,Address,Gender)
    print(dtel.displayrecord())
    

    



