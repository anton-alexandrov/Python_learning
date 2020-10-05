
myfile = open ('my_file.txt')
print('First time read file: \n\t'+myfile.read())

# when we try to read the same file one more time, it will be empty. This happens because
# you can imagine the reading "cursor" is at the end of the file after having read it.
# So there is nothing left to read. We can reset the "cursor" like this: myfile.seek(0)
print('Second time read file: \n\t' + myfile.read())
myfile.seek(0)
print('Third time read file: \n\t' + myfile.read())


# read the file by lines
myfile.seek(0)
print('Second line: '+myfile.readlines()[1])

#we have to close file when we done
myfile.close()

#another way to work with file without closing it manualy:
with open('my_file.txt') as myfile:
    print('Third line: \n\t' + myfile.readlines()[2])

with open('my_file.txt') as myfile:
    for ID, line in enumerate(myfile):
        print (str(ID) +". "+ line)
#file modes
# with open('my_file.txt', mode = 'r') as myfile: read only the file
# with open('my_file.txt', mode = 'w') as myfile: write only the file
# with open('my_file.txt', mode = 'a') as myfile: append only the file
# with open('my_file.txt', mode = 'r+') as myfile: read and write the file
# with open('my_file.txt', mode = 'w+') as myfile: write and read only the file. Owerwrites existing file OR creates a new file if the file doesn't exists!
with open('my_file.txt', mode = 'w') as f:
        f.write('This is a first line\n')
        f.write('This is a second line\n')
        f.write('This is a third line\n')

with open('my_file.txt', mode='a') as f:
    f.write('This is a fourth line\n')