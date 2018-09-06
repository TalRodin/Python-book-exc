
class CashRegister:
    def __init__(self):        
        self.__list_item=[]
    def purchase_item(self, RetailItem):
        self.__list_item.append(RetailItem)        
    def get_total(self):
        total=0.0
        for i in self.__list_item:
            total+=i.__get_price()
        return total
    def show_items(self):
        for i in self.__list_item:
            print(i.get_item_description())
    def clear(self):
        for i in self.__list_item:
            self.__list_item.remove(i)