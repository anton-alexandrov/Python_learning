def capitals(word):
    #return ( [i for i in range(len(word)) if word[i].isupper()])
    #your code here
    n=0
    res=[]
    for i in word:
        if i == i.upper():
            res.append(n)
            n+=1
        else:
            n+=1
    return res


print(capitals('CodEWaRs'))

# , [0, 3, 4, 6]