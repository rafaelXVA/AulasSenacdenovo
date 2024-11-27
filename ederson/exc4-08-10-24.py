num=int(input("quantity of apples: "))
if num > 11:
    price=num*0.25
    print("item        quantity         price\n"+"-"*35+"\napple      %d             %.2f"%(num,price))
else:
    price=num*0.30
    print(f"item        quantity         price\n"+"-"*35+"\napple      %d             %.2f"%(num,price))