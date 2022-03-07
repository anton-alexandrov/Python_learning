from bs4 import BeautifulSoup
import requests



url="https://www.youtube.com/watch?v=et-i4geFG2s&list=PL6Gtav8N4O7j1Ri5uXMaQs-7agQG7p0cG&index=1&t=9s"
site = requests.get(url)
print(f"Response code: {site.status_code}")

siteObjects = BeautifulSoup(site.content,"html.parser")
print(siteObjects)

#views = siteObjects.find_all(class_ ="") #find by class



#Local file

#htmlfile = open("skillbox.html", "rb") # Открыть файл, положить его в переменную htmlfile
#code = htmlfile.read() # Получить все содержимое файла в переменную code
#soup = BeautifulSoup(code,"html.parser")  # Разобрать html-код на элементы
#links = soup.findAll("a") # Найти все элементы "a" - т.е. ссылки

#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#for i in soup.find_all('a'):
#  print (i.string.strip())
