def descending_order(num):
    # Bust a move right here
    res=''
    for i in sorted(str(num), reverse = True):
        res = res+i
    return int(res)
#or return int("".join(sorted(str(num), reverse=True)))

print(descending_order(15))
print(descending_order(123456789))