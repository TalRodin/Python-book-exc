class CashRegister:
    def __init__(self):
        self.__list=[]
    def purchase_item(self, retailItem):
        self.__list.append(retailItem)
    def get_total(self):
        total=0.0
        for i in self.__list:
            total+=i.get_price()
        return total
    def show_items(self):
        for i in self.__list:
            print(i.get_item_description())
    def clear(self):
        for i in self.__list:
            self.__list.remove(i)