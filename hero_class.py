class Hero():
    """Create a Hero"""
    def __init__(self, name, level, race):
        self.name = name
        self.level = level
        self.race = race
        self.health=100
        #super().__init__()
    
    def show_hero (self):
        description = ("Name is: "+self.name + "\n\tLevel is " + str(self.level) + " " 
        + "\n\tRace is: " +self.race 
        + " \n\tHealth is: " + str(self.health))
        print (description)

    def level_up (self):
        self.level+=1
    
    def move (self):
        print ("Hero " + self.name + " start moving...")
    
    def set_health (self, new_health):
        self.health=new_health

class SuperHero (Hero):
    """inherit class from existent one"""
    def __init__(self, name, level, race, magic):
        super().__init__(name, level, race)
        self.magic = magic
        self.magic = 100
    
    def make_magic(self):
        self.magic -=10
    
    def show_hero(self):
        description = (self.name + "'s level is " + str(self.level) + " " + "from " +self.race + " has health " + str(self.health) + " and magic" + str(self.magic)  )
        print (description)
