from urllib import request, parse
# import requests
import sys

site1 = "https://sunduchokknig.com/search?"
value = {'q':"Носов"}

#site1 = "https://www.google.com/search?"
#value = {'q':"Witcher"}
myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
myheader['Accept'] = "text/html"

try:
    mydata = parse.urlencode(value)
    print("Mydata" + str(mydata))
    site1 = site1+mydata
    print("Mysite: "+ site1)
    req =request.Request(site1, headers=myheader)
    print("Request: " + str(req))
    response = request.urlopen(req)
    print("Request 1" + str(request))
    # print("".join([str(line) for line in response.readlines()]))
    html = response.read().decode(response.headers.get_content_charset())
    with open("something.html", "w") as f:
        f.write(html)
    print(html)
    print("Request 2" + str(request))
    # for line in response:
    #     print(line)
except (Exception, ) as e:
    print("Error has occured")
    print(e)
