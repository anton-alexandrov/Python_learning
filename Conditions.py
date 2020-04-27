age = 1

if (age <= 2):
    print ("You are baby")
elif (age>2) and (age<5):
    print("You are todler")
elif (age>=5) and (age<10):
    print ("You are kid")
elif (age>=10) and (age<=19):
    print("You are teenager")
else:
    print ("You are adult")


print ("++++++++++++++++")

all_cars = ['lada', 'toyota','honda', 'bmw','mercedes', 'fiat']
japanese_cars = ['honda', 'toyota', 'accura']

if 'lada' in all_cars:
    print ("Lada is in the list")
else: 
    print ("Lada IS NOT in the list")

for car in all_cars:
    if car in japanese_cars:
        print (car.title() + " is Japanese car")
    else:
        print (car.title()+ " is NOT Japanese car")