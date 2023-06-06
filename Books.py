class Book : 
    def __init__ (self,BookId,Name,Author,Category,IssueDate=0,DueDate=0,Status=0,IssuedBy=0):
        self.Book_id = int(BookId)
        self.Book_id += 1
        self.Name = Name
        self.Author = Author
        self.Category = Category
        self.Status = Status
        self.IssuedById = IssuedBy
        self.IssueDate = IssueDate
        self.DueDate = DueDate
    
    def __str__ (self):
        data = str(self.Book_id)+(" ")*(8-len(str(self.Book_id)))+"| "+str(self.Name)+(" ")*(
            33-len(str(self.Name)))+"| "+str(self.Author)+(" ")*(
                30-len(str(self.Author)))+"| "+str(self.Category)+(" ")*(
                            20-len(str(self.Category)))+"| "+str(self.Status)+(" ")*(
                                6-len(str(self.Status)))+"| "+str(self.IssueDate)+(" ")*(
                                    10-len(str(self.IssueDate)))+"|"+str(self.DueDate)+(" ")*(
                                    9-len(str(self.DueDate)))+"|"+str(self.IssuedById)+(" ")*(
                                    13-len(str(self.IssuedById)))
        return data

    def diplayrecord (self):
        print("*******************************")
        print("Book id : ", self.Book_id)
        print("Name of the book : ",self.Name)
        print("Author Name : ",self.Author)
        print("Publication House Name : ",self.Publication)
        print("Publication Year : ",self.PublicationYear)
        print("Category of a Book : ",self.Category)
        print("--------------------------------")


if (__name__ == "__main__"):
    Name = input("Enter Name Here : ")
    Author = input("Enter Author Name Here : ")
    Publication = input("Enter Publication Name Here : ")
    PublicationYear = input("Enter a Publication Date Here : ")
    Category = input("Enter a Book Category : ")
    dtel = Book(Name,Author,Publication,PublicationYear,Category)
    print(dtel.diplayrecord())