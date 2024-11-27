a=80000
b=200000
anos=0
while True:
    aNow=a+(a*0.03)
    bNow=b+(b*1.5/100)
    a=aNow
    b=bNow
    anos=anos+1
    if aNow==bNow:
        print(f"o país A com {a:.0f} pessoas\npassou B com {b:.0f} pessoas")
        print(f"em um processo que demorou {anos} anos")
        break