k = raw_input ("Please enter your name: ")
print ("Hi " + k)

#input always reads strings
num1= raw_input("Please enter a: ")
num2 = raw_input ("Please enter b:")
summa = int(num1)+int(num2)
print (summa)


message =""
while True:
    message = raw_input("Please enter a password...")
    if message =="password":
        break
    else:
        print("Password is not correct")



#fill Array from keyboard
my_list = []
message = ""

while message!='stop':
    message = raw_input ("Please enter next item or stop: ")
    my_list.append(message)
print (my_list)