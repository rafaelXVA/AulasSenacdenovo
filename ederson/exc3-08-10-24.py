import os
password=1234
passwordEnt=int(input("enter your password\n"))
os.system("cls")
if passwordEnt == password:
    print("access allowed")
else:
    print("access denied")
while password != passwordEnt:
    passwordEnt=int(input("try again\n"))
    os.system("cls")
    if passwordEnt == password:
        print("access allowed")
    else:
        print("access denied")