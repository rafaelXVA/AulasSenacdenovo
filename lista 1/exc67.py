def gmail(email):
    arroba = False
    pont = False
    before = False
    after = False
    
    for i, char in enumerate(email):
        if char == '@':
            if arroba:  
                return False
            arroba = True
            before = i > 0
        if char == '.':
            if arroba: 
                pont = True
            after = arroba and i < len(email) - 1
        
    if arroba and pont and before and after:
        return True
    return False

email = "osakamuitofoda@gmail.com"
print({gmail(email)})