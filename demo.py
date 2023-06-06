from libraryMgmntSstm import Mngmnt
''' 
m = line.strip()
print(m)
print(type(m))

with open("Book.txt","r") as Book:
            Book.seek(327,0)
            for line in Book:
                m = line.split("|")
                x = m[0]
                print(x)

str_1 = "  Hire freelance developers              "
x = (str_1.strip())
print(x)

NameOfBook = "CHAWA"
Manager = Mngmnt()
Books = []
found = False
with open("Book.txt","r") as Book:
    #Line by read
    for line in Book:
        data = line.split(",")
        mm = data.strip()
        if (NameOfBook == mm[1]) and (mm[-2] != "1"):
                print(mm[-2])
                print(mm[-1])

NameOfBook = "CHAWA"
with open("Book.txt","r") as Book:
    #Line by read
    k = Book.seek(286,0)
    for line in Book:
        data = line.split("|")
        x = data[1].strip()
        if x == NameOfBook :
            print("Yess")
            break
        else:
            print("Noooooo")
            break
'''

# Driver code
s = [['DATTA', 'M', '12-05-12', '9970089138', 'SAMBHAJINAGAR', '900001', '2022-12-28 09:12:26.636238', '2023-01-12 09:12:26.636238', '16001', 'Datta07', 'firstbit\n']]
str1 = ""
# traverse in the string
print(s[0][-1])
for ele in range (0,len(s[0])-1):
    if ele != -1:
        print(s[ele])
    else:
        print(s[ele])
print(str1)






