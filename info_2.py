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

