try:
    a=int(input("digite uma palabvra: "))
except ValueError:
    print("digite apenas números")
except:
    print("erro desconhecido")
finally:
    print("final do algoritmo   ")