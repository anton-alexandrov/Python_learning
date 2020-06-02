def abbrevName(name):
    name = name.title()
    first_name, last_name = name.split()
    #return('{}.{}'.format(first_name[0], last_name[0]))
    return (f"{first_name[0]}.{last_name[0]}")


print(abbrevName("Sam Smith"))
print(abbrevName("eddy baurer"))