def animal_crackers(text):
    """ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter"""
    return text.split(" ")[0][0] == text.split(" ")[1][0].upper()

print (animal_crackers('Levelheaded Llama'))

def old_macdonald(name):
    """OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name"""
    #opt 1
    mylist = list(name)
    mylist[0]=mylist[0].upper()
    mylist[3]=mylist[3].upper()
    print("".join(mylist))

    #opt2
    print (name[0].upper()+name[1:3]+name[3].upper()+name[4:])

    #opt 3
    str = []
    for i in range (0, len(name)):
        if i==0 or i==3:
            str.append(name[i].upper())
        else:
            str.append(name[i].lower())
    return "".join(str)
print(old_macdonald('macdonald'))

def master_yoda(text):
    """MASTER YODA: Given a sentence, return a sentence with the words reversed"""
    return " ".join(text.split(" ")[::-1])

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

print('---------')
def has_33(nums):
    """Given a list of ints, return True if the array contains a 3 next to a 3 somewhere."""
    for n in range (0,len(nums)-1):
        if nums[n]==nums[n+1]==3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 3,3]))

print(has_33([1, 3, 1, 3]))

print('+++++++++++++++')

def spy (nums):
    """SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order"""
    my_list = [str(x) for x in nums if x ==0 or x==7]
    string = "".join(my_list)
    if '007' in string:
        return  True
    return False
print(spy([1,2,4,0,0,7,5]))
print(spy([1,0,2,4,0,5,7]))
print(spy(([1,7,2,0,4,5,0])))