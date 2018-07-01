# chapter 10

#1

class Pet:
    #__name = "";
    #__animal_type = "";
    #__age = 0;
    def __init__(self,name,animal_type,age):
        self.__name=name
        self.__animal_type=animal_type
        self.__age=age
        
    def set_name(self,name):
        self.__name=name
    def set_animal_type(self,animal_type):
        self.__animal_type=animal_type
    def set_age(self,age):
        self.__age=age
    
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
    


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
#car.py
class Car:

    def __init__(self,year_model,make,speed):
        self.__year_model=year_model
        self.__make=make
        self.__speed=speed
        
    def set_year_model(self, year_model):
        self.__year_model=year_model
    def set_make(self,make):
        self.__make=make
    def set_speed(self,speed):
        self.__speed=speed
        
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

#car2.py    
#import car
def main():
        
    year_model=input("Please enter the model: ")
    
    make=input("Plese enter the make: ")
    
    speed=int(input("Please enter speed: " ))
    
    
    c=Car(year_model, make,speed)
    for i in range(5):
        f=c.accelerate()
    print(f)
    
    for i in range(5):
        b=c.brake()
    print(b)
            
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
#import info
def main():
    
     data=make_info_list()
#    print(data)
     display(data)
        
def make_info_list():
    list_=[]
    
    print("Enter information: ")
    for i in range(1,4):
        name=input("Name: ")
        address=input("Address: ")
        age=input("Age: ")
        phone_number=input("Phone number: ")
        print()
    
        inf=Info(name, address, age, phone_number)
        list_.append(inf)
    return list_
def display(list_):
    print("Name " +' '+ "Address "+' '+ "Age "+' '+ "Phone number ")
    for item in list_:
        
        print(item.get_name(),' ',item.get_address(),' ',item.get_age(), ' ',item.get_phone_number() )
        
        print()
main()


#4
#info.py
class Employee:
    def __init__(self, name, ID_number, Department, Job_title):
        self.__name=name
        self.__ID_number=ID_number
        self.__Department=Department
        self.__Job_title=Job_title
        
        
    def set_name(self, name):
        self.__name=name
        
    def set_ID_number(self, ID_number): 
        self.__ID_number=ID_number
        
    def set_Department(self, Department): 
        self.__Department=Department
        
    def set_Job_title(self, Job_title): 
        self.__Job_title=Job_title   
        
                
    def get_name(self):
        return (self.__name)
    def get_ID_number(self):
        return (self.__ID_number)
    def get_Department(self):
        return (self.__Department)
    def get_Job_title(self):
        return (self.__Job_title)
#info__2.py
#import info_
def main():
    
     data=make_Employee()
#    print(data)
     display(data)
def make_Employee():
    list_=[]
    
    print("Enter information: ")
    for i in range(1,4):
        name=input("Name: ")
        ID_number=input("ID_number: ")
        Department=input("Department: ")
        Job_title=input("Job_title: ")
        print()
    
        inf=Employee(name, ID_number, Department, Job_title)
        list_.append(inf)
    return list_    

  
    
def display(list_):
    print("Name " +' '+ "ID_number "+' '+ "Department "+' '+ "Job_title ")
    for item in list_:
        
        print(item.get_name(),' ',item.get_ID_number(),' ',item.get_Department(), ' ',item.get_Job_title() )
        
        print()

main()


#5

class RetailItem:
    def __init__(self, Description, Units, Price):
        self.__Description=Description
        self.__Units=Units
        self.__Price=Price      
        
        
    def set_Description(self, Description):
        self.__Description=Description
        
    def set_Units(self, Units): 
        self.__Units=Units
        
    def set_Price(self, Price): 
        self.__Price=Price
        
                
    def get_Description(self):
        return (self.__Description)
    def get_Units(self):
        return (self.__Units)
    def get_Price(self):
        return (self.__Price)



def main():
    
     data=make_RetailItem()
#    print(data)
     display(data)
def make_RetailItem():
    list_=[]
    
    print("Enter information: ")
    for i in range(1,4):
        Description=input("Description: ")
        Units=input("Units: ")
        Price=input("Price: ")        
        print()
    
        inf=RetailItem(Description, Units, Price)
        list_.append(inf)
    return list_    
    
def display(list_):
    print(' '+"Description " +' '+ "Units "+' '+ "Price ")
    for item in list_:
        
        print(' ', item.get_Description(),' ',item.get_Units(),' ',item.get_Price() )
        
        print()

main()



#6

class Employee:
    def __init__(self, name, ID_number, Department, Job_title):
        self.__name=name
        self.__ID_number=ID_number
        self.__Department=Department
        self.__Job_title=Job_title
        
        
    def set_name(self, name):
        self.__name=name
        
    def set_ID_number(self, ID_number): 
        self.__ID_number=ID_number
        
    def set_Department(self, Department): 
        self.__Department=Department
        
    def set_Job_title(self, Job_title): 
        self.__Job_title=Job_title   
        
                
    def get_name(self):
        return (self.__name)
    def get_ID_number(self):
        return (self.__ID_number)
    def get_Department(self):
        return (self.__Department)
    def get_Job_title(self):
        return (self.__Job_title)
    
    def  __str__(self):
        return 'ID Number: '+ self.__ID_number +\
               '\nName: '+ self.__name+\
               '\nDepartment: '+ self.__Department+\
               '\nJob_title: '+ self.__Job_title
#info__2.py
#import info_
def main():
    
     data=make_Employee()
     
     print(data)
     d=display(data)
     
     look_up(d)
def make_Employee():
    list_=[]
    
    print("Enter information: ")
    for i in range(1,4):
        name=input("Name: ")
        ID_number=input("ID_number: ")
        Department=input("Department: ")
        Job_title=input("Job_title: ")
        print()
    
        inf=Employee(name, ID_number, Department, Job_title)
        list_.append(inf)
    return list_    

  
    
def display(list_):
    dict_empl={}
    for item in list_:
        dict_empl[item.get_ID_number()]=[item.get_name(),item.get_Department(),item.get_Job_title() ]


    
    return(dict_empl)
    print("Name " +' '+ "ID_number "+' '+ "Department "+' '+ "Job_title ")
    
    for item in list_:
        
        print(item.get_name(),' ',item.get_ID_number(),' ',item.get_Department(), ' ',item.get_Job_title() )
        
        print()
       
def look_up(d):
    print('1. Look up an employee in the dictionary. ')
    print('2. Add a new employee to the dictionary. ')
    print("3. Change and existing employee's name, department, and job title in the dictionary. ")
    print('4. Delete an employee from the dictionary. ')
    print('5. Quit the program. ')
    choice=int(input("Enter your choice: "))
    if choice==1:
        ID=input("Enter the ID of employee: ")
        print(d[ID])
    elif choice==2:
        
        name=input("Name: ")
        ID_number=input("ID_number: ")
        Department=input("Department: ")
        Job_title=input("Job_title: ")
        print()
        
        new_inf=Employee(name, ID_number, Department, Job_title)
        
        
        
    elif choice==3:
        ID_to_change=input("Please enter the ID of employee to change info: ")
        employee_to_work_with=d[ID_to_change]
        print(employee_to_work_with)
        print('What do you want to change: ')
        print('1. Name')
        print('2. Department')
        print('3. Job_title')
        print('Please enter your choice: ')
        choice=input()
        if choice==1:
            new_name=input("Please enter the new name: ")
            
            d['Name']=new_name
        elif choice==2:
            new_department=input("Please enter the new department: ")
            
            d['Department']=new_department
            
        elif choice==3:
            new_job_title=input("Please enter the new job title: ")
            d['Job_title']=new_job_title
        
    elif choice==4:
        id_=input("Enter the ID number of employee to delete: ")
        del d[id_]
        print(d)
    elif choice==5:
        quit
    else:
        print('Error')
    

main()

#7



#8

