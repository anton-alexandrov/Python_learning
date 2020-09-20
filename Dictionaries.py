#create dictionary
enemy = {
    'loc_x':70, #item
    'loc_y':40, #key:value
    'color':'green',
    'health':100,
    'name':'enemy1'
}
print(enemy)
print(enemy.keys())
print(enemy.values())

print ("Location X: "+str(enemy['loc_x']))
print ("Location Y: "+str(enemy['loc_y']))
print ("Name is: "+ enemy['name'])

#add new item
enemy['level'] = 1

#delete item
del enemy ['level']

#update item
enemy ['loc_x'] = enemy ['loc_x'] + 40
enemy['health'] = enemy['health']-30
if enemy['health']<80:
    enemy['color']='yellow'

print (enemy['loc_x'])
print (enemy['health'])
print (enemy['color'])

#array of dictionaries
all_enemies = []
for x in range (0,10):
    #all_enemies.append(enemy) --all objects will be the same, if we change one, all others will be changed
    all_enemies.append(enemy.copy()) #create object like, not the same
    all_enemies[x]['name']= 'Name '+str(x)
    all_enemies[x]['loc_x']= x*10

for enemy in all_enemies:
    print (enemy)
