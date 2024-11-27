while True:
    a=int(input("quantida de pessoas no país A: "))
    b=int(input("quantidade de pessoas no país B: "))
    taxaA=float(input("taxa de crescimento do país A: "))
    taxaB=float(input("taxa de crescimento do país B: "))
    yearsP=int(input("anos para simulação: "))
    anos=0
    import os
    while True:
        aNow=a+(a*(taxaA/100))
        bNow=b+(b*(taxaB/100))
        a=aNow
        b=bNow
        anos=anos+1
        if anos==yearsP:
            print(f"o país A possuí {a:.0f} pessoas\no país B possuí {b:.0f}")
            print(f"em {anos} anos")
            break
    if taxaB>taxaA and b>a:
        print("o país A nunca passaria o país B")
    elif b>a: 
        while True:
            aNow=a+(a*(taxaA/100))
            bNow=b+(b*(taxaB/100))
            a=aNow
            b=bNow
            anos=anos+1
            if aNow>bNow:
                print(f"o país A com {a:.0f} pessoas\npassaria o país B com {b:.0f} pessoas")
                print(f"em um processo de {anos} anos")
                break
    if taxaA>taxaB and a>b:
        print("o país B nunca passaria o país A")
    elif a>b:
        while True:
            aNow=a+(a*(taxaA/100))
            bNow=b+(b*(taxaB/100))
            a=aNow
            b=bNow
            anos=anos+1
            if bNow>aNow:
                print(f"o país b com {b:.0f} pessoas\npassaria o país A com {a:.0f} pessoas")
                print(f"em um processo de {anos} anos")
                break   
    end=str(input("você quer encerrar o programa ou continuar? (E/C)"))
    if end=="E":
        os.system("cls")
        break
    elif end=="C":
        os.system("cls")
        continue