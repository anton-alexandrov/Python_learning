number = 9119

array = str(number)
result=[]

res=''
for i in str(number):
  result.append(int(i)**2)


for i in result:
    res = res + str(i)
print (res)


#Solution
#def square_digits(num):
#    ret = ""
#    for x in str(num):
#        ret += str(int(x)**2)
#    return int(ret)