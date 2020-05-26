def derive(coefficient, exponent):
    # your code here
    #return(str(coefficient*exponent)+'x^'+str(exponent-1))
    return f'{coefficient * exponent}x^{exponent - 1}'

print(derive(7,8))