def horner (number, system):
    my_list=[]
    n = number
    while n > 0:
       my_list.append(n%system)
       n //= system
    string = [str(x) for x in my_list[::-1]]
    print("".join(string))
    return int ("".join(string))



print(horner(194,5))

x = 0b111101
y = 0o123
t = int('111101', 2)
print(x, y, t)
print(bin(61))
print(oct(83))
print(hex(61))

def hello_sep (name = 'World', sep = '-'):
    print("Hello", name, sep=sep)
def hello (name='Karl'):
    print("Hello", name)
hello_sep()
hello_sep("John")
hello()