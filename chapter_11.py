#1
class Employee:
    def __init__(self, employee_name, employee_number):
        self.employee_name=employee_name
        self.employee_number=employee_number
        
    def set_employee_name(self, employee_name):
        self.employee_name=employee_name
    def set_employee_number(self, employee_number): 
        self.employee_number=employee_number
        
    def get_employee_name(self):
        return self.employee_name
    def get_employee_number(self):
        return self.employee_number
    
class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):
        Employee.__init__(self,employee_name, employee_number)
        self.shift_number=shift_number
        self.hourly_pay_rate=hourly_pay_rate
        
    def set_shift_number(self, shift_number):
        self.shift_number=shift_number
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.hourly_pay_rate=hourly_pay_rate
        
    def get_shift_number(self):
        return self.shift_number
    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate

#2    
#2    
class ShiftSupervisor(Employee):
    def __init__(self, employee_name, employee_number, annual_salary, bonus):
        Employee.__init__(self, employee_name, employee_number)
        self.annual_salary=annual_salary
        self.bonus=bonus
    
    def set_annual_salary(self, annual_salary):
        self.annual_salary=annual_salary
    def set_bonus(self, bonus):
        self.bonus=bonus
        
    def get_annual_salary(self):
        return self.annual_salary
    def get_bonus(self):
        return self.bonus
    
def main():
    name=input("Enter the name: ")
    number=int(input("Enter the number: "))
    shift_number=int(input("Enter the shift number (1,2,3): "))
    rate=float(input("Enter the hourly rate: "))
    e=ProductionWorker(name,number,shift_number,rate)
    print(e.get_employee_name())
    print(e.get_employee_number())
    print(e.get_shift_number())
    print(e.get_hourly_pay_rate())
main() 

#for problem #2
#def main():
#    name=input("Enter the name: ")
#    number=int(input("Enter the number: "))
#    super_salary=float(input("Enter super salary: "))
#    bonus=float(input("Enter the bonus: "))
#    e=ShiftSupervisor(name,number,super_salary,bonus)
#    print(e.get_employee_name())
#    print(e.get_employee_number())    
#    print(e.get_annual_salary())
#    print(e.get_bonus())
#main() 


#3

class Person:
    def __init__(self, name, address, phone_number):
        self.name=name
        self.address=address
        self.phone_number=phone_number
    
    def set_name(self, name):
        self.name=name
    def set_address(self, address):
        self.address=address 
    def set_phone_number(self, phone_number):
        self.phone_number=phone_number
    
    def get_name(self, name):
        return self.name
    def get_address(self, address):
        return self.address
    def get_phone_number(self, phone_number):
        return self.phone_number  
        
class Customer(Person):
    def  __init__(self,name, address, phone_number, customer_number, mailing_list):      
        Person.__init__(self,name, address, phone_number)
        self.cusomer_number=customer_number
        self.mailing_list=mailing_list
        
    def set_customer_number(self, customer_number):
        self.customer_number=customer_number
        
    def set_mailing_list (self, mailing_list ):
        self.mailing_list=mailing_list   
        
    def get_customer_number(self, customer_number):
        return self.customer_number   
        
    def get_mailing_list(self, mailing_list):
        return self.mailing_list    
        
        
def main():
    name=input("Enter the name: ")
    address=input("Enter the address: ")
    phone_number=input("Enter the phone number: ")
    customer_number=int(input("Enter the customer number: "))
    mailing_list=bool(input('Enter yes or no:'))
    e=Customer(name,address,phone_number,customer_number,mailing_list)
    print(e.get_name())
    print(e.get_address())
    print(e.get_phone_number())
    print(e.get_customer_number())
    print(e.get_mailing_list())

main()         
        
        
        
        
        