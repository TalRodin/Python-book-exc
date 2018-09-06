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
    def __init__(self, name, ID_number, department, job_title):
        self.__name=name
        self.__ID_number=ID_number
        self.__department=department
        self.__job_title=job_title
        
    def set_name(self, name):
        self.__name=name
    def set_ID_number(self,ID_number):
        self.__ID_number=ID_number
    def set_department(self, department):
        self.__department=department
    def set_job_title(self, job_title):
        self.__job_title=job_title
        
    def get_name(self):
        return self.__name
    def get_ID_number(self):
        return self.__ID_number
    def get_department(self):
        return self.__department
    def get_job_title(self):
        return self.__job_title
        
    def  __str__(self):
        return "Name: "+self.__name+\
               "\nID number: "+ self.__ID_number+\
               "\nDepartment: "+ self.__department+\
               "\nJob title: "+self.__job_title
#info__2.py
#import info_
import empl
import pickle

LOOK_UP=1
ADD=2
CHANGE=3
DELETE=4
QUIT=5

FILENAME='Python_problems_book/employee.dat'

def main():
    employees_=load_employees()
    choice=0
    while choice!=QUIT:
        choice=get_menu_choice()
        
        if choice==LOOK_UP:
            look_up(employees_)
        elif choice==ADD:
            add(employees_)
        elif choice==CHANGE:
            change(employees_)
        elif choice==DELETE:
            delete(employees_)
    save_contacts(employees_)               
        
def load_employees():
    try:
        input_file=open(FILENAME, 'rb')
        employee_dct=pickle.load(input_file)
        input_file.close()
    except IOError:
        employee_dct={}
    return employee_dct    
        
def  get_menu_choice():
    print()
    print('Menu:')
    print('---')
    print('1. Look up a contact')
    print('2. Add a new contact')
    print('3. Change an existing contact')
    print('4. Delete a contact')
    print('5. Quit the program')
    print()
    
    choice=int(input('Enter your choice: '))
    
    while choice < LOOK_UP or choice > QUIT:
        choice=int(input('Enter a valid choice: '))
        
    return choice
    
def look_up(employees_):
    ID=input('Enter a ID: ')
    
    print(employees_.get(ID, 'That ID is not found.'))
    
def add(employees_):
    employee=input().split()
    

    em=empl.Employee(employee[0],employee[1],employee[2],employee[3])
        
    if employee[0] not in employees_:
        employees_[employee[1]]= em
        print('The entry has been added.')
    else:
        print('That name already exists.')

def change(employees_):
    ID=input('Enter a ID: ')
    if ID in employees_:
        name=input('Enter the new name: ')
        
        department=input('Enter the new department: ')
        
        job_title=input('Enter the new Job title: ')
        
        entry=empl.Employee(ID,name,department,job_title)
        
        employees_[ID]=entry
        print('Information updated.')
        
    else:
        print('That name is not found.')
        
def delete(employees_):
    ID=input('Enter a ID: ')
    if ID in employees_:
        del employees_[ID]
        print('Entry deleted.')
        
    else:
        print("That ID is not found.")
 
def save_contacts(employees_):
    output_file=open(FILENAME, 'wb')
    pickle.dump(employees_, output_file)  
    output_file.close()
     
main()

#7

class RetailItem:
    def __init__(self,item_description, units_inventory, price):
        self.__item_description=item_description
        self.__units_inventory=units_inventory
        self.__price=price
        
    def set_item_description(self,item_description):
        self.__item_description=item_description
    def set_units_inventory(self,units_inventory):
        self.__units_inventory=units_inventory
    def set_price(self, price):
        self.__price=price
        
    def get_item_description(self):
        return self.__item_description
    def get_units_inventory(self):
        return self.__units_inventory
    def get_price(self):
        return float(self.__price)
    
    
class CashRegister:
    def __init__(self):        
        self.__list_item=[]
    def purchase_item(self, RetailI):
        self.__list_item.append(RetailI)        
    def get_total(self):
        total=0.0
        for i in self.__list_item:
            total+=i.get_price()
        return total
    def show_items(self):
        for i in self.__list_item:
            print(i.get_item_description())
    def clear(self):
        for i in self.__list_item:
            self.__list_item.remove(i)    
    
def main():

    item_1=input().split()
    item_2=input().split()
    item_3=input().split()
    
    
    ret_I_1=RetailItem(item_1[0],item_1[1],item_1[2])
    ret_I_2=RetailItem(item_2[0],item_2[1],item_2[2])
    ret_I_3=RetailItem(item_3[0],item_3[1],item_3[2])
    
    cash_register=CashRegister()
    print(ret_I_1.get_item_description())
    print(ret_I_2.get_item_description())
    print(ret_I_3.get_item_description())
    
    
    keep_going='Y'
    while keep_going=='Y':
        print('Enter the item, you would like to buy: ', end=' ')
        item=input()
        if item.upper()==ret_I_1.get_item_description().upper():
            cash_register.purchase_item(ret_I_1)
        elif item.upper()==ret_I_2.get_item_description().upper():
            cash_register.purchase_item(ret_I_2)
        elif item.upper()==ret_I_3.get_item_description().upper():
            cash_register.purchase_item(ret_I_3)
        keep_going=input('Enter "Y" to continue: ')
        
    print('Total: ')
    #print(cash_register.show_items())
    print(cash_register.get_total())
main()


#8

