# range

print(list(range(0,11,2)))

# enumerate
# enumerate returns tuple. We can unpack tuple
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))

print(list(enumerate('abcde')))
#zip. quickly create a list of tuples by "zipping" up together two lists.
list1 = [0, 1, 2]
list2 = ['a', 'b', 'c']
list3 = [10, 20, 30]

print(list(zip(list1, list2, list3)))

for i in zip(list1, list2, list3):
    print(i)