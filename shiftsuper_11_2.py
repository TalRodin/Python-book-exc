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
    #shift_number=int(input("Enter the shift number (1,2,3): "))
    #rate=float(input("Enter the hourly rate: "))
    super_salary=float(input("Enter super salary: "))
    bonus=float(input("Enter the bonus: "))
    e=ShiftSupervisor(name,number,super_salary,bonus)
    print(e.get_employee_name())
    print(e.get_employee_number())    
    print(e.get_annual_salary())
    print(e.get_bonus())
    
main() 

