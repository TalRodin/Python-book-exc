#1

class Poodle(Dog):
    
#2

class Plant:
    def __init__(self, plant_type):
        self.__plant_type=plant_type
    def message(self):
        print("I'm a plant.")
class Tree(Plant):
    def __init__(self):
        Plant.__init__(self, 'tree')
    def message(self):
        print("I'm a tree.")


p=Plant('sampling')
t=Tree()
p.message() # prints 'I'm a plant'
t.message() # prints 'I'm a tree'

#3

class Beverage:
    def __init__(self, bev_name):
        self.__bev_name=bev_name
        
class Cola(Beverage):
    def __init__(self, bev_name, cola)
         Beverage.__init__(self, bev_name)
         self.cola=cola