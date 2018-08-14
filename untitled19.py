def main():

    print("1. Look up a person's email: ")
    print("2. Add a new name and email address: ")
    print("3. Change an existing email address: ")
    print("4. Delete an existing name and email address: ")
    choice=int(input())
    return choice


def look_up(email_addresses):
    name=input("Enter name: ")
    print(email_addresses.get(name, "Not found."))
def add(email_addresses):
    name=input("Enter name: ")
    e_address=input("Enter email address: ")
    
    if name not in email_addresses:
        email_addresses[name]=e_address
    else:
        print('This name exists.')
        
        
        
def change(email_addresses):
    name=input("Enter the name: ")
    if name in email_addresses:
        email=input("Enter the new email: ")
        email_addresses[name]=email
    
    else:
        print("That name is not found.")
        
def delete(email_addresses):
    
    name=input("Enter the name: ")
    if name in email_addresses:
        del email_addresses[name]
    else:
        print("That name is not found.") 

if __name__=='__main__':
    
    LOOK_UP=1
    ADD=2
    CHANGE=3
    DELETE=4
    QUIT=5
    
    email_addresses={}
    
    choice=0
    
    while choice!=QUIT:
        
        choice=main()
        
        if choice==LOOK_UP:
            look_up(email_addresses)
        elif choice==ADD:
            add(email_addresses)
        elif choice==CHANGE:
            change(email_addresses)
        elif choice==DELETE:
            delete(email_addresses)

            
        









































