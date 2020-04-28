# how to create
def func_name(name):
    """description"""
    print ("Hello, "+name)
    print ("How are you?")
    answer = raw_input ("Please enter fine / not fine: ")
    if answer=="fine":
        print("Glad to see you are fine, "+name)
    elif answer=="not fine":
       print( "Oh, I'm sorry")
    else:
        print("Sorry, I didn't get it")
name = raw_input ("What's your name? ")
func_name(name)

#finction wih 2 parameters
def summa (x,y):
    print ("Summa:" + str(x+y))

summa (9,11)

#return
def diff (x,y):
    return x-y

print("Difference is: "+str(diff(10,3)))

#factorial function
def factor(n):
    """Calculate factor of n"""
    i=1
    result=1
    #while i<=n:
    while i in range (1,n+1):
        result = i*result
        i=i+1
    print("Factor of " + str(n)+" is "+ str(result))

factor (3)
factor (4)
factor (5)


#create dictionary in function
def create_user (name, phone, address):
    record = {
        'name':name,
        'phone':phone,
        'address':address
    }
    return record

user1 = create_user("User name 1", "+9712787868", "Dallas, TX")
user2 = create_user ("Iser name 2", "212134343", "Raleigh, NC")

print(user1)
print(user2)

