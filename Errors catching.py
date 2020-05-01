import sys

filename = './Input files/namesk.txt'
try:
    print ("We are inside TRY block")
    myfile = open (filename, mode = 'r', encoding='utf-8')
    for line in myfile:
        print(line)
except Exception:
    print ("Now we are in EXCEPT block")
    print("File not found")
    print("Error is \n\t"  +  str(sys.exc_info()))
else:
    print(myfile)
finally:
    print ("Inside FINALLY")

print("---------------EOF--------------")