import os

#balance,password
account=[0,55471926]
option=1
os.system("cls")
passwordconf=int(input("enter your password\n"))
os.system("cls")
if passwordconf==account[1]:
    while option != 0:
        print("select an option")
        print("1-balance")
        print("2-deposit amount")
        print("3-withdraw amount")
        print("0-exit\n")
        option=int(input("enter here: "))
        os.system("cls")
       
       
       
        if option==1:
            print("you have an amount of ",account[0])
            back=int(input("enter 0 to go back to menu: "))
            os.system("cls")
            if back==0:
                os.system("cls")
            else:
                back=int(input("only 0 allowed\nenter 0 to go back to menu: "))
                os.system("cls")
                while back!=0:
                    back=int(input("only 0 allowed\nenter 0 to go back to menu: "))
                    os.system("cls")
       
       

        elif option==2:
            deposit=int(input("enter 0 to cancel action\nmount to deposit: "))
            account[0]=deposit+account[0]
            os.system("cls")
            if deposit>0 or deposit<0:
                print("your new balance is: ",account[0])
                back=int(input("enter 0 to go back to menu: "))
                os.system("cls")
                if back==0:
                    os.system("cls")
                while back!=0:
                    back=int(input("only 0 allowed\nenter 0 to go back to menu: "))
            elif deposit==0:
                print("action canceled")
                back=int(input("enter 0 to go back to menu: "))
                os.system("cls")
                if back==0:
                    os.system("cls")
                while back!=0:
                    back=int(input("only 0 allowed\nenter 0 to go back to menu: "))
                    os.system("cls")


        elif option==3:
            withdraw=int(input("enter 0 to cancel action\nmount to withdraw: "))
            account[0]=account[0]-withdraw
            os.system("cls")
            if withdraw>0:
                print("your new balance is: ",account[0])
                back=int(input("enter 0 to go back to menu: "))
                os.system("cls")
                if back==0:
                    os.system("cls")
                while back!=0:
                    back=int(input("only 0 allowed\nenter 0 to go back to menu: "))
            elif withdraw==0:
                print("action canceled")
                back=int(input("enter 0 to go back to menu: "))
                os.system("cls")
                if back==0:
                    os.system("cls")
                while back!=0:
                    back=int(input("only 0 allowed\nenter 0 to go back to menu: "))
                    os.system("cls")
            elif withdraw>account[0]:
                print("you can't withdraw more than you have")
                back=int(input("enter 0 to go back to menu: "))
                if back==0:
                    os.system("cls")
                while back!=0:
                    back=int(input("only 0 allowed\nenter 0 to go back to menu: "))
                    os.system("cls")
else:
    print("hello world!")