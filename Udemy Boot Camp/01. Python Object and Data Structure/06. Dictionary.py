#in dictionaties objects retrieved by key name. Dict is unsorted and can't be sorted
my_dict = {'k1':'value1', 'k2':10, 'k3':[0,1,2,3,4,5,6], 'k4':{'internalKey':'internal Value'}}
print(my_dict['k1'])
print(my_dict['k3'][2:6])
print(my_dict['k4']['internalKey'])


#adding new element
my_dict['k5'] = 'added element'
print(my_dict)

#updating element
my_dict['k5'] = 'updated element'
print(my_dict)

#getting list of values / keys
print(my_dict.values())
print(my_dict.keys())

if 'Apple' not in my_dict.values():
    n = len(my_dict.keys())
    print(n)
    my_dict['k'+str(n+1)] = 'Apple'
print(my_dict)

#creating a empty dict
d = {}

#create a list from values
list_of_values = list(my_dict.values())
print (list_of_values)


