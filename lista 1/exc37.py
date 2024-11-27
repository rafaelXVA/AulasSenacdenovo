def perfect(n):
    div = []
    for i in range(1, n):
        if(n%i==0):
            div.append(i)
    
    if(n == sum(div)):
        return 'GOOD MAN'
    else:
        return 'paia'
    
print(perfect(496))