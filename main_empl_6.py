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