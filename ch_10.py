# chapter 10

#1

class Pet:
    #__name = "";
    #__animal_type = "";
    #__age = 0;
    def __init__(self,name,animal_type,age):
        self.__name=name;
        self.__animal_type=animal_type;
        self.__age=age;
        
    def set_name(self,name):
        self.__name=name;
    def set_animal_type(self,animal_type):
        self.__animal_type=animal_type;
    def set_age(self,age):
        self.__age=age;
    
    def get_name(self):
        return self.__name;
    def get_animal_type(self):
        return self.__animal_type;
    def get_age(self):
        return self.__age;
    


def main():
    
    name=input("Please enter the name: ")
    
    animal_type=input("Plese enter the animal type: ")
    
    age=input("Please enter age: " )
    
    
    p=Pet(name, animal_type, age)
  
    print("Name: ", p.get_name())
    print("Animal type: ", p.get_animal_type())
    print("Age: ", p.get_age())

main()
    
#2

class Car:
    #__name = "";
    #__animal_type = "";
    #__age = 0;
    def __init__(self,year_model,make,speed):
        self.__year_model=year_model
        self.__make=make
        self.__speed=0
        
    def set_year_model(self, year_model):
        self.__year_model=year_model
    def set_make(self,make):
        self.__make=make
    def set_speed(self,speed):
        self.__speed=0
        
    def get_year_model(self):
        return self.__speed
    def get_make(self):
        return self.__speed
  
    #methods
    def accelerate(self):
        self.__speed=self.__speed+5
        return self.__speed
    def brake(self):
        self.__speed=self.__speed-5
        return self.__speed
    def get_speed(self):
        return self.__speed
    
def main():
        
    year_model=input("Please enter the model: ")
    
    make=input("Plese enter the make: ")
    
    speed=input("Please enter speed: " )
    
    
    c=Car(year_model, make,speed)
    for i in range(5):
        print(c.accelerate())
    
    for i in range(5):
        print(c.brake())
            
main()
 
#3
#info.py
class Info:
    def __init__(self, name, address, age, phone_number):
        self.__name=name
        self.__address=address
        self.__age=age
        self.__phone_number=phone_number
        
    def set_name(self, name):
        self.__name=name
    def set_address(self, address):
        self.__address=address
    def set_age(self, age):
        self.__age=age
    def set_phone_number(self, phone_number):
        self.__phone_number=phone_number
        
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self): 
        return self.__age
    def get_phone_number(self):
        return self.__phone_number

#info_2.py
import info
def main():
    
     data=make_info_list()
#    print(data)
     display(data)
        
def make_info_list():
    list_=[]
    
    print("Enter information: ")
    for i in range(1,6):
        name=input("Name: ")
        address=input("Address: ")
        age=input("Age: ")
        phone_number=input("Phone number: ")
        print()
    
        inf=info.Info(name, address, age, phone_number)
        list_.append(inf)
    return list_
def display(list_):
    for item in list_:
        
        print("Name: ", item.get_name())
        print("Address: ", item.get_address())
        print("Age: ",item.get_age())
        print("Phone number: ",item.get_phone_number())
        print()
main()


#4


#5
#6
#7
#8
