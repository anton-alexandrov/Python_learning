from bs4 import BeautifulSoup

htmlfile = open("skillbox.html", "rb") # Открыть файл, положить его в переменную htmlfile
code = htmlfile.read() # Получить все содержимое файла в переменную code
soup = BeautifulSoup(code,"html.parser")  # Разобрать html-код на элементы

links = soup.findAll("a") # Найти все элементы "a" - т.е. ссылки

print(soup.title)
print(soup.title.name)
print(soup.title.string)
for i in soup.find_all('a'):
  print (i.string.strip())
# print([item.string.strip() for item in links]) # Вывести текст каждой ссылки
