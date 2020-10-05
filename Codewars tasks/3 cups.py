from random import shuffle

def shuffle_list(cups):
    shuffle(cups)
    print(cups)
    choise(cups)
    return cups

def choise (cups):
    while True:
        n = int(input('What cup:? \n'))
        if cups[n] == 1:
            print ('You got it')
            break
        else:
            print("Try again")



my_list = [0,0,1]

m = input("Do you want to play? (y/n): \n")
if m == 'y':
    print('playing')
    shuffle_list(my_list)
else:
    print('not playing')


while m == 'y':
    m = input("Do you want to play again? (y/n): \n")
    if m == 'y':
        print('playing again')
        shuffle_list(my_list)
    else:
        print('Bye')