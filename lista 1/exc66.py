def bin2dec(binario):
    decimal = 0
    binario2 = []
    for i in range(len(binario)- 1,-1, -1):
        binario2.append(binario[i])
    for i in range(0, len(binario2)):
        decimal+= int(binario2[i])*(2**i)
    return decimal
binario = "110"
print(bin2dec(binario))