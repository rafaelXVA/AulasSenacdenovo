def all(x):
    if x>0:
        return "P"
    elif x<0:
        return "N"
    else:
        return "0"
while True:
    num=int(input("numero: "))
    if all(num)=="P":
        print("P")
    elif all(num)=="N":
        print("N")
    else:
        print("0")