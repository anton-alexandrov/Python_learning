
all_cars = ['lada', 'toyota','honda', 'bmw','mercedes', 'fiat']
japanese_cars = ['honda', 'toyota', 'accura']


for car in all_cars:
    if car in japanese_cars:
        print (car.title() + " is Japanese car")
    else:
        print (car.title()+ " is NOT Japanese car")

# iterate if we don't need variable
for _ in 'Hello World':
    print ("Cool!")

#Tuples have a special quality when it comes to for loops.
# If you are iterating through a sequence that contains tuples,
# the item can actually be the tuple itself, this is an example of tuple unpacking.
# During the for loop we will be unpacking the tuple inside of a sequence and we can access the individual items inside that tuple!

list_of_tuples = [(1, 2), (3, 4), (5, 6), (7, 8)]
for item in list_of_tuples:
    print((item))
k=1
for a, b in list_of_tuples:
    print(f"First  element in {k} tuple: {a}")
    print(f'Second element in {k} tuple: {b}')
    k+=1

#iterate the dictionary
#by default we got only keys

dict = {'k1':'v1', 'k2':'v2', 'k3':'v3'}
for item in dict:
    print(item)

#to get values
for item in dict.values():
    print(item)

#to get all items
for item in dict.items():
    print(item)

# the same as default
for item in dict.keys():
    print(item)

#item in dictionary is tuple
for key,value in dict.items():
    print(f'{key}::{value}')


#for loop
for i in range (0,10):
    print (i)

print ("----------")

#including last value
for i in range (0, 5 + 1):
    print (i)

# incremental value
print ("----------")
for i in range (0,10, 2):
    print (i)

# pass key word. Pass allows to run the code further doing nothing. Used as a placeholder

for i in range (0, 5):
    pass
print('This ^ will be done later')

# continue key word. Goes to the top of the closest enclosing loop.
for letter in "Sammy":
    if letter == 'a':
        continue
    print(letter)

# break key word. Breaks out of the current enclosing loop.
for letter in "Sammy":
    if letter == 'a':
        break
    print(letter)