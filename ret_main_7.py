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
   