one=int(input())
two=int(input())
three=int(input())
if one > two > three:
    print(one,two,three) #321
elif one > three > two:
    print(one,three,two) #312
elif two > one > three:
    print(two,one,three) #231
elif two > three > one:
    print(two,three,one) #132
elif three > one > two:
    print(three,one,two) #213
elif three > two > one:
    print(three,two,one) #123