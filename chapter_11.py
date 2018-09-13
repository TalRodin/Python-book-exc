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
def main():
    name=input("Enter the name: ")
    number=int(input("Enter the number: "))
    shift_number=int(input("Enter the shift number: "))
    rate=int(input("Enter the hourly rate: "))
    e=ProductionWorker(name,number,shift_number,rate)
    
main()    