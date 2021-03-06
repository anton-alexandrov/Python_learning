first_list = ['one', 'two', 'three']
second_list  = ['four', 'five']

#list could contain different data types
my_list = ['String', 10, 10.02]

#double the list
print(my_list*2)

#we can concatenate lists
new_list = first_list + second_list
print(new_list)

#list is mutable, we can change any element
new_list[0] = 'ONE'
print(new_list)

#we can slice lists
print(new_list[2:5])

#add element
new_list.append('six')
print(new_list)

# delete element
popped_item = new_list.pop()
print(popped_item)
print(new_list)

#sorting  / reverse
unsorted_list = ['a', 'e', 'd', 'b', 'c']
unsorted_list.sort() #doesn't return anything, we cann't do print(unsorted_list.sort())
print(unsorted_list)
unsorted_list.reverse()
print(unsorted_list)

#list comprehension. ALternative way to create a list from some iterable object: string, range, list
my_list = [x for x in 'Hello World!']
print(my_list)

my_list = [x**2 for x in range(0,11) if x%2 == 0]
print(my_list)

celsius = [0,10,20.1,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius ]
print(fahrenheit)

#count number of repetions of element in list
my_list = [1,2,3,4,1,2,5,6]
print(f'Number 1 repeats {my_list.count(1)} times')

