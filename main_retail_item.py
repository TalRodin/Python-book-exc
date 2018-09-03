import ret_item

def main():
    
    item1=input().split()
    item2=input().split()
    item3=input().split()
    
    i1=ret_item.RetailItem(item1[0],item1[1],item1[2])
    i2=ret_item.RetailItem(item2[0],item2[1],item2[2])
    i3=ret_item.RetailItem(item3[0],item3[1],item3[2])
    
    print('--'*10)
    print(' '*4,'Description',' ','Units in Inventory',' ','Price')
    print('--'*10)
    print('Item #1',i1.get_item_description(),' '*5,i1.get_units_inventory(),' '*5, i1.get_price())
    print('Item #2',i2.get_item_description(),' '*5,i2.get_units_inventory(),' '*5, i2.get_price())
    print('Item #3',i3.get_item_description(),' '*5,i3.get_units_inventory(),' '*5, i3.get_price())
main()