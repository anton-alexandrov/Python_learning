#Brute force
def if_number_simple (x):
    """return False if the number is not simple, and True if simple"""
    for n in range  (2,x):
        if x % n == 0:
            return False
    return True

def factorize_num (num):
    #factors = [x for x in range(2,num) if if_number_simple(num) == False and num%x == 0]
    factors=[]
    x=2
    while num>1:
        if num%x==0:
            factors.append((x))
            num//=x
        else:
            x+=1
    return factors


print(f'The number 6 is simple: {if_number_simple(6)}')
print(f'The number 17 is simple: {if_number_simple(17)}')
print(f'The number 15 is simple: {if_number_simple(15)}')

print(f'Number 15 could be factirized as {factorize_num(15)}')
print(f'Number 17 could be factirized as {factorize_num(17)}')
print(f'Number 999 could be factirized as {factorize_num(999)}')