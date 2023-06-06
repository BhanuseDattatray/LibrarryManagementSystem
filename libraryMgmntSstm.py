from Student import Student
from Librarian import Librarian
from Books import Book
import datetime
class Mngmnt:
    AnyID = 0
    User = 0
    Step = 0
    def CardNo(self):
        with open ("Student.txt","a") as m :
            q = m.tell()
            if (q != 0 ):
                with open ("Student.txt","r") as k:
                    for line in k:
                        x = line.split(",")  
                    return x[-3]
            else:
                return 16000
              
    def Student_Title(self):
        Name = input("Enter Name Here : ").upper()
        DOJ = input("Enter Date of Join Here : ")
        MobileNo = input("Enter a Mobile No Here : ")
        Address = input("Enter a Address : ").upper()
        Gender = input("Enter a Gender : ")
        Username = input("Enter Username : ")
        Password = input("Enter a Password : ")
        Manager = Mngmnt()
        CardNo = Manager.CardNo()
        dtel = Student(Username,CardNo,Name,DOJ,MobileNo,Address,Gender,Password)
        return dtel
    
    def AddStudent(self):
        Manager = Mngmnt()
        print("i am in Add Student")
        dtel = Manager.Student_Title()
        with open("Student.txt","a") as k:
            data = str(dtel)
            k.write(data)
            k.write("\n")

    def Libra_IdGenerator(self):
        with open ("librarian.txt","a") as m :
            q = m.tell()
            print("i am in libra id generator for libra")
            if (q) != 0 :
                with open ("librarian.txt","r") as k:
                    for line in k:
                        x = line.split(",")
                    return x[-3]
            else:
                return 0

    def Libra_Title(self):
        Manager = Mngmnt()
        SerialNo =  Manager.Libra_IdGenerator()
        Name = input("Enter Name Here : ").upper()
        DOJ = input("Enter Date of Join Here : ")
        MobileNo = input("Enter a Mobile No Here : ")
        Address = input("Enter a Address : ").upper()
        Gender = input("Enter a Gender : ").upper()
        Username = input("Enter Username : ")
        Password = input("Enter a Password : ")
        dtel = Librarian(SerialNo,Username,Name,DOJ,MobileNo,Address,Gender,Password)
        return dtel

    def AddLibra(self): 
        Manager = Mngmnt()
        dtel = Manager.Libra_Title()
        with open("Librarian.txt","a") as k:
            data = str(dtel)
            k.write(data)
            k.write("\n")


    def ShowLibra(self,Username):
        U = Username
        with open ("librarian.txt","a") as m :
            q = m.tell()
            if (q) != 0 :
                with open ("librarian.txt","r") as k:
                    for line in k:
                        x = line.split(",")
                        if (U == x[-2]):
                            d = "  |  ".join(x)
                            print(d)
                            break
                        else: 
                            return False
            else:
                return "No Data Found"
        

    def ShowStudent(self,Username):
        U = Username
        with open ("Student.txt","a") as m :
            q = m.tell()
            if (q) != 0 :
                with open ("Student.txt","r") as k:
                    for line in k:
                        x = line.split(",")
                        if (U == x[-2]):
                            d = " | ".join(x)
                            print(d)
                            break
                        else: 
                            return False
            else:
                return "No Data Found"

    
    def VerifyStd(self,Username,Password):
        U = Username
        P = Password
        try:
            with open ("Student.txt","r") as k:
                for line in k:
                    x = line.split(",")
                    y = x[-1][0:-1]
                    if (U == x[-2] and P == y):
                        return True
                        break
                    else: 
                        return False
        except FileNotFoundError:
            print("File does not exist")
    
    def VerifyLibra(self,Username,Password):
        U = Username
        P = Password
        try:
            with open ("librarian.txt","r") as k:
                for line in k:
                    Linesplit = line.split(',')
                    print(Linesplit)
                    print(Linesplit[-1])
                    print(Username,Password)
                    if (Password+'\n' in Linesplit and Username in Linesplit):
                        return True
                        break
                    else: 
                        return False
        except FileNotFoundError:
            print("File does not exist")
                        
    # Book Section Start From Here 
    def BookIdGnrtr(self):
        with open("Book.txt","a") as Book:
            x = Book.tell()
            if (x > 329):
                with open("Book.txt","r") as Book:
                    for line in Book:
                        n = line.split("|")
                    return n[0]
            else: 
                return 900000
                

    def AddBook(self):
        Manager = Mngmnt()
        BookID = Manager.BookIdGnrtr()
        Name = input("Enter Book Name Here : ").upper()
        Author = input("Enter Author Name Here : ").upper()
        Category = input("Enter a Book Category : ").upper()
        dtel = Book(BookID,Name,Author,Category)

        with open ("Book.txt","a") as m :
            q = m.tell()
            if (q) != 0 :
                with open("Book.txt","a") as b:
                    data = str(dtel)
                    b.write(data)
                    b.write("\n")
            else:
                with open("Book.txt","a") as b:
                    data = str("Book Id")+(" ")*(8-len("Book Id"))+"| "+str("Name")+(" ")*(
                        33-len(str("Name")))+"| "+str("Author")+(" ")*(
                            30-len(str("Author")))+"| "+str("Category")+(" ")*(
                                        20-len(("Category")))+"| "+("Status")+(" ")*(
                                           6-len(str("Status")))+"| "+str("Issue Date")+(" ")*(
                                              6-len(str("Issued Date")))+"| "+str("Due Date")+(" ")*(
                                              6-len(str("Due Date")))+"| "+str("Issued By Id")+(" ")*(
                                              6-len(str("Issued By Id")))+"\n"+("-"*8)+"|"+(
                                                "-"*34)+"|"+("-"*31)+"|"+("-"*21)+"|"+("-"*7)+"|"+("-"*11)+"|"+(
                                                    "-"*9)+"|"+("-"*13)

                    b.write(data)
                    b.write("\n")
                    beta = str(dtel)
                    b.write(beta)
                    b.write("\n")        

    # This Function fetches all books available in database
    def GetAll_Avail_Books(self):
        with open ("Book.txt","a") as m :
            q = m.tell()
            if (q) != 0 :
                with open ("Book.txt","r") as k:
                    for line in k:
                        print(line)
            else:
                return "No Data Found"
    # This Function Create a Entry of Student into books database Issue Register.
    def BookCardEntry(self,BookId,UserID,bookid,Issuedate,Duedate):
        currentdate = datetime.datetime.now()
        DueDate = str(currentdate + datetime.timedelta(days=15))
        IssueDate = str(currentdate)
        Status = 1
        BookId = BookId
        buklst = []
        with open("Book.txt","r") as Book:
            #Line by read
            k = Book.seek(286,0)
            for line in Book:
                data = line.split("|")
                x = data[0].strip()
                bookid = data[0].strip()
                Found = False
                if (BookId == x):
                    Found = True
                    data[-1] = +"|"+str(UserID)+(" ")*(13-len(str(UserID)))
                    data[-2] = +"|"+str(DueDate)+(" ")*(9-len(str(DueDate)))
                    data[-3] = +"| "+str(IssueDate)+(" ")*(10-len(str(IssueDate)))
                    data[-4] = +"| "+str(Status)+(" ")*(6-len(str(Status)))
                    line = "|".join(x)
                    buklst.append(line)
                else:
                    line = "|".join(line)
                    buklst.append(line)
            if (Found):
                with open("Data.txt","w") as fp:
                    for bk in buklst:
                        fp.write(bk)
            else:
                print("Record not present")
                

    def GetBookByName(self,NameOfBook,Username):
        try:
            Manager = Mngmnt()
            found = False
            NameOfBook = NameOfBook
            with open("Book.txt","r") as Book:
                #Line by read
                k = Book.seek(286,0)
                for line in Book:
                    data = line.split("|")
                    if (NameOfBook in data):
                        import datetime
                        currentdate = datetime.datetime.now()
                        Duedate = str(currentdate + datetime.timedelta(days=15))
                        Issuedate = str(currentdate)
                        bookid = 0
                        EntryToStdReg = Manager.BookCardEntry(Username,bookid,Issuedate,Duedate)
                        break
                    else:
                        print("Noooooo")
                        break
        except FileNotFoundError:
            print("File does not exist")  


    def UpdateBook(self,):
        pass

    def DeleteBook(self,):
        pass