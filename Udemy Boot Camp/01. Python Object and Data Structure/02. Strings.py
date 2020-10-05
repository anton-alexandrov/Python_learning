#String is ordered sequence of characters
#Strings are immutable

name = "anTON aleksandrov"



print ("Second letter: "+name[1])

#reverse index
print ("Last letter: "+name[-1])

#slicing
print ("Slice from 2 to 5 with step 1: "+name[2:5:1])
print ("Slice from 2 to the end: "+name[2:])
print ("Slice from 2 to the end with step 2: "+name[2::2])
print ("Slice from the beginning to 8 with step 2: "+name[:8:2])
print ("Slice from the beginning to the end with step 2: "+name[::2])
print ("Reverse the string: "+name[::-1])


print ("Name: " + name.title())
print ("Upper case: " + name.upper())
print("Lower case: " + name.lower())

print("Line 1 \nLine 2")
print("Messages: \n\tMessage 1\n\tMessage 2")

#how to cut symbols in string 
text = "   ...text....   "
# delete spaces
print (text.strip())
#then delete dotes
print (text.strip().strip(".")) 