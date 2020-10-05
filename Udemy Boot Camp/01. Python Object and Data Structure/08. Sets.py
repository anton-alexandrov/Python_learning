#Sets are an unordered collection of unique elements.

my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(2)


#cast list to set to remove repeted elements
my_list = [1,1,1,2,2,2,2,3,3,3,3,3,]
print(my_list)
my_set = set(my_list)
print((my_set))
