def myfunc (str):
    mylist = []
    for x in range (0, len(str)):
        if x%2==0:
            mylist.append(str[x].lower())
        else:
            mylist.append(str[x].upper())

    return "".join(mylist)

print(myfunc('Anthropomorphism'))
