
cities = ['First City', 'Moscow', 'London', 'new york', 'Toronto', 'Raleigh', 'Cary']
print(cities)

print ("Length of Array: "+str(len(cities)))

#print Array
i=0
while i<len(cities):
    print (cities[i])
    i = i+1

#from the end of Array
print ("-2 index:"+ cities[-2])

print (cities[3].title())
cities[3]=cities[3].title()

# change in Array
cities[2] = 'Tula'

#add new item to the end of Array
cities.append('Kursk')
print (cities)

#add new item in the middle of Array
cities.insert(1, 'Tokyo')
print(cities)

#delete from the Array by position
del cities [2]
del cities[-1]
print(cities)

#delete by value
cities.remove('Tula')
print(cities)

#delete to somewhere
deleted_city = cities.pop()
print ("Deleted city is: " + deleted_city)
print (cities)

#sorting
cities.sort()
print ("Sorted list: ")
print (cities)
cities.sort(reverse=True)
print ("Reversed sorted list:" ) 
print (cities)

#for loop for Arrays
cars = ['volvo', 'chevy', 'porshe', 'honda', 'toyota']
for car in cars:
    print (car.title())

#get part of Array
mycars = cars[1:4]
mycars1 = cars [0:3]
mycars2 = cars [-3:]
mycars3 = cars [-3:-1]
print(mycars)
print(mycars1)
print(mycars2)
print(mycars3)


#create numeric Array
my_number_list = list(range(0,10))
print (my_number_list)

#change numeric Array in loop
for x in my_number_list:
    x= x*2
    print (x)

#Max, Min, Sum
print("Max number: " +str(max(my_number_list)))
print ("Sum of list is: " + str(sum(my_number_list)))

#copy of Array
mycars = cars #if we change cars, mycars will be changed as well
mycars1 = cars[:] #if we change cars, mycars1 WON'T be changed
cars.append('accura')
print (cars)
print (mycars)
print (mycars1)


my_list = []
for x in [2, 4, 6]:
    for y in [1, 10, 100]:
        my_list.append(x*y)
print(my_list)

F = [0]*10
F[1] = 'a'
F[5] = 5
print(F)