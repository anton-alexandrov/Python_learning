def parse(arr):
    message = input('Input message: ')
    for i in range (0, len(message.split("|")), 1):
        print(arr[i] + ": "+ message.split("|")[i])




def print1 ():
    option = ""
    while option != 'stop':
        option = input("Enter option or type stop: ")
        if option == '1':
            print1_1()
        elif option == '2':
            print1_2()


def print1_1 ():
    arr = ["1.1", "1.2", "1.3"]
    parse(arr)

def print1_2 ():
    arr = ["1.2.1", "1.2.2", "1.2.3"]
    parse(arr)

def print2 ():
    arr = ["2.1", "2.2", "2.3"]
    parse(arr)


option = ""

while option!='stop':
    option = input ("Enter option or type stop: ")
    if option == '1':
        print1()
    elif option == '2':
        print2()

