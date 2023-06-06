from libraryMgmntSstm import Mngmnt

Manager = Mngmnt()  # Student, stafff, and librarian Answer
Answer = 0
while (Answer < 3):
    print()
    print('''Pick Who You Are From Options \n\n\t\t1) Student - Type1 1. \t\t 2) for Librarian - Type 2. \n \n\t\t3) for To Close Tab - Type 3''')
    print()
    try:
        Answer = int(input("Please Enter  : "))
    except ValueError:
        print("invalid literal for int() with base 10:")
    else:
        if (Answer == 1):
            "\n"
            print('''\n\t\t1. Student Login  \t\t\t2. New Student...Signup  \n\n\t\t3. Return to main menu \t\t\t4. Close''')
            print()
            choice = int(input("Student Please Enter Your Choice Here : "))
            if (choice == 1):
                Username = input("Enter Your Username Number Here : ")
                Password = input("Enter Your Password Here : ")
                Verify = Manager.VerifyStd(Username, Password)
                print(" Credential Found...!!!!!", Verify)
                if (Verify):
                    print()
                    print('''\t\t1. Issue Book \n\t\t2. Return Book\n\t\t3. Fines''')
                    print()
                    STDchoice = int(input("Enter Your Choice Here : "))
                    if (STDchoice == 1):
                        Manager.GetAll_Avail_Books()
                        print("This are the available books you can get")
                        print(
                            '''\n1. Please Enter a Book Name : ''')
                        try:
                            NameOfBook = input("Enter a Book Name : ").upper()
                            Manager.GetBookByName(NameOfBook, Username)
                        except ValueError:
                            print('Book Name Should Not Be a Number :')
                        except:
                            print('This Book Is Not Available...!')
                        else:
                            pass   
                    elif (STDchoice == 3):
                        print("Return a book")
                        pass
            elif (choice == 2):
                Manager.AddStudent()
                print(
                    "\n\t\t\tYour Credentials have succesfully added.....Please SignIn ")

        elif (Answer == 2):
            Lchoice = 0
            while (Lchoice < 3):
                print()
                print('''\t\t\t Welcome To FirstBit College of Computer Science Pune\n\n\t\t1) For Login Type-1.\t\t2) For Signup\t\t 3) Return To Main Window''')
                print()
                print("\t\t\t\t\tFor Librarian only")
                print()
                try:
                    Lchoice = int(input("Please Enter Your Choice Here : "))
                except ValueError:
                    print('invalid Choice Please Type Correc Number...!')
                    Answer = 2
                else:
                    if (Lchoice == 1):
                        try:
                            Username = input("Enter Your Username Here : ")
                            Password = input("Enter Your Password Here :")
                        except ValueError:
                            print("invalid literal for int() with base 10:")
                        else:
                            libra = Manager.VerifyLibra(Username, Password)
                            if (libra):
                                Libra_SignInChoices = 0
                                while (Libra_SignInChoices < 7):
                                    print(
                                        '''1. Profile   2. Add a Book   3. Show All Available Books   4. Update a Book   5. Delete a Book   6. Search a Book  7. Issuers Register 8. LogOut''')
                                    Libra_SignInChoices = int(input("Please Enter Your Choice : "))
                                    if (Libra_SignInChoices == 1):
                                        x = Manager.ShowLibra(Username)
                                        print(x)
                                    elif (Libra_SignInChoices == 2):
                                        Manager.AddBook()
                                        print(
                                            '''This Book Is Successfull Added To Library..''')

                                    elif (Libra_SignInChoices == 3):
                                        Manager.GetAll_Avail_Books()

                                    elif (Libra_SignInChoices == 4):
                                        Manager.UpdateBook()

                                    elif (Libra_SignInChoices == 5):
                                        Manager.DeleteBook()
                                        # Ithe If else banav jyane aplyala samjel ki book sapadla ani pudhe kay karaych
                                    else:
                                        print("Invalid Choice....Try Again.....!!!")
                    elif (Lchoice == 2):
                            Manager.AddLibra()
                            print("\t\t\t\tSucessfull SignUp")
                            print(
                                "\nPlease Login With Newly Generated Username and Password... Thank You")
                            Answer = 2
                    else:
                        print("\t\t\t\t\tInvalid Choice....!! Try Again")
                        Answer = 2
