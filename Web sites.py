from urllib import request, parse
import sys

site1 = "https://sunduchokknig.com/search?"
value = {'q':"Носов"}

#site1 = "https://www.google.com/search?"
#value = {'q':"Witcher"}
myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

try:
    mydata = parse.urlencode(value)
    print("Mydata" + str(mydata))
    site1 = site1+mydata
    print ("Mysite: "+ site1)
    req  =request.Request(site1, headers=myheader)
    print("Request: " + str(req))
    response = request.urlopen(req)
    print ("Request 1" + str(request))
    response = response.readlines()
    print ("Request 2" + str(request))
    for line in response:
        print(line)
except Exception:
    print("Error has occured")
    print (sys.exc_info()[1])
