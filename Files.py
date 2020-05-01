#path to file
input_file = './Input files/names.txt'
output_file = './Input files/out.txt'
# modes: r-read, w-write (create new file each time), a-add (add to existent file)
myfile = open(input_file, mode='r', encoding='utf_8')
my_out_file = open(output_file, mode='w', encoding='utf-8') 

#print enumarated list of lines
for ID, line in enumerate(myfile):
    print (str(ID) + ". Name: " + line.strip()) 

print ("++++++++++++++")

#start numeration from 1 and if statement
myfile = open(input_file, mode='r', encoding='utf_8')
for ID, line in enumerate(myfile,1): 
    if "Anton" in line:
        print (str(ID) + ". Name: " + line.strip()) 
        my_out_file.write(line)
myfile.close()


