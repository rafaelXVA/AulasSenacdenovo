def apaga(s):
    text = ''
    vogals = ''
    for i in range(0, len(s)):
        if s[i] == 'a' or s[i] == 'A' or s[i] == 'e' or s[i] == 'E' or s[i] == 'i' or s[i] == 'I' or s[i] == 'o' or s[i] == 'O' or  s[i] == 'u' or s[i] == 'U' or s[i] == 'á' or s[i] == 'Á' or s[i] == 'é' or s[i] == 'É' or s[i] == 'í' or s[i] == 'Í' or s[i] == 'ó' or s[i] == 'Ó' or s[i] == 'ú' or s[i] == 'Ú':
            vogals += s[i]
        else:
            text += s[i]
    print(s)
    return text
    
    
print(apaga('COEEEE CARA CHAPOU' ))