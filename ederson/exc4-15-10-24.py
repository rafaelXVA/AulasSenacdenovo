import os
suspect=0
q1=str(input("Telefonou para a vítima?\n"))
if q1.upper()=="SIM":
    suspect=suspect+1
q2=input("Esteve no local do crime?\n")
if q2.upper()=="SIM":
    suspect=suspect+1
q3=input("Mora perto da vítima?\n")
if q3.upper()=="SIM":
    suspect=suspect+1
q4=input("Devia para a vítima?\n")
if q4.upper()=="SIM":
    suspect=suspect+1
q5=input("Já trabalhou com a vítima?\n")
if q5.upper()=="SIM":
    suspect=suspect+1
if suspect<2:
    print("A pessoa é inocente")
elif suspect==2:
    print("A pessoa é suspeita")
elif suspect==3 or suspect==4:
    print("A pessoa é cúmplice")
elif suspect==5:
    print("A pessoa é o assassino")