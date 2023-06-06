from Personal_details import PrsnlDtel
class Librarian(PrsnlDtel) : 
    def __init__ (self,SerialNo,UserName,Name,DOJ,MobileNo,Address,Gender,Password):
        super().__init__ (Name,DOJ,MobileNo,Address,Gender)
        self.SerialNo = int(SerialNo)
        self.SerialNo += 1
        self.Libraian_UserName = UserName
        self.Password = Password
    
    def __str__ (self):
        data = super().__str__() + str(self.SerialNo)+","+str(self.Libraian_UserName)+","+str(self.Password)
        return data 
    
    def diplayrecord (self):
        super().displayrecord()
        print("Staff id : ", self.Id)
        print("Password : ",self.Password)
        print("--------------------------------")

if (__name__ == "__main__"):
    Name = input("Enter Name Here : ")
    Branch = input("Enter Branch Name Here : ")
    DOJ = input("Enter Date of Join Here : ")
    MobileNo = input("Enter a Mobile No Here : ")
    Address = input("Enter a Address : ")
    Gender = input("Enter a Gender : ")
    Department = input("Enter a Book Year : ")
    Password = input("Enter a Password : ")
    dtel = Librarian(Name,Branch,DOJ,MobileNo,Address,Gender,Department,Password)
    print(dtel.diplayrecord())
    








