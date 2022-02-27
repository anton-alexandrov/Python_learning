import json

datafile = open("webinars.json", "rb") # Открыли файл, пложили его в переменную datafile
data = json.load(datafile) # Прочитать данные из файла в формате json, в переменную data

for item in data: # Для каждого вебинара в переменной data вывести speaker'а
  print(item["speaker"])

  