from Personal_details import PrsnlDtel
class Student(PrsnlDtel) : 
    def __init__ (self,Username,CardNo,Name,DOJ,MobileNo,Address,Gender,Password,bookid=0,issuedate=0,duedate=0):
        super().__init__ (Name,DOJ,MobileNo,Address,Gender)
        self.CardNo = int(CardNo)
        self.CardNo += 1
        self.bookid = bookid
        self.issuedate = issuedate
        self.duedate = duedate
        self.Username = Username
        self.Password = Password
    
    def __str__ (self):
        data = super().__str__() + str(self.bookid)+","+str(self.issuedate)+","+str(self.duedate)+","+str(self.CardNo)+","+ str(self.Username)+","+str(self.Password)
        return data
    
    def diplayrecord (self):
        super().displayrecord()
        print("Student id : ", self.Id)
        print("Year of education : ",self.Year)
        print("Password : ",self.Password)
        print("--------------------------------")

if (__name__ == "__main__"):
    Id = input("Enter a User Name Here: ")
    Name = input("Enter Name Here : ")
    DOJ = input("Enter Date of Join Here : ")
    MobileNo = input("Enter a Mobile No Here : ")
    Address = input("Enter a Address : ")
    Gender = input("Enter a Gender : ")
    Year = input("Enter a Book Year : ")
    Password = input("Enter a Password : ")
    dtel = Student(Id,Name,DOJ,MobileNo,Address,Gender,Year,Password)
    print(dtel.diplayrecord())
    print(dtel)
    








