import ret_item

def main():
    x=int(input('Enter number of items: '))
    print(' '*6,'Description',' ','Units in Inventory',' ','Price') 
    for i in range(x):
        item=input().split()
        j=ret_item.RetailItem(item[0],item[1],item[2])
        print('Item #',i+1,': ', j.get_item_description(),' '*10,j.get_units_inventory(),' '*5, j.get_price())

    
          

main()