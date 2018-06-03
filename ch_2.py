#chapter 2

#1

def main():
    print("Name\nAddress\nPhone Number\nCollege Major")   
main()

#2

def main():
    total_sales= input("Please, enter the total sales: ")
    annual_profit=0.23*int(total_sales)
    print('Annual profit: $', annual_profit)
main()

#3

def main():
    one_acre_land=43560
    square_feet=input("Enter the total square fee in a tract of land: ")
    print("The number of acres in the tract: ", format(int(square_feet)/one_acre_land, '.2f'))
main()

#4
 
def main():
    #items=5
    price_1=int(input("Price 1st item: "))
    price_2=int(input("Price 2nd item: "))
    price_3=int(input("Price 3rd item: "))
    price_4=int(input("Price 4th item: "))
    price_5=int(input("Price 5th item: "))
    subtotal_cost=price_1+price_2+price_3+price_4+price_5
    tax=0.07*subtotal_cost
    total=subtotal_cost+tax
    print("\nSubtotal cost: ", subtotal_cost )
    print("Tax: ", format(tax, '.2f'))
    print("Total cost: ", total)
main()

#5

def main():
    speed=70
    #distance=speed*time
    print('\nDistance in 6 hours: ', speed*6)
    print('Distance in 10 hours: ', speed*10)
    print('Distance in 15 hours: ', speed*15)       
main()

#6

def main():
    amount_purchase=int(input('Enter the amount of a purchase: '))
    state_sales_tax=0.05
    county_sales_tax=0.025
    print('Amount of purchase: ', amount_purchase)
    print('State sales tax: ', format(state_sales_tax*amount_purchase, '.2f'))
    print('County sales tax: ', format(county_sales_tax*amount_purchase, '.2f'))
    print('Total taxes: ', format(state_sales_tax*amount_purchase+county_sales_tax*amount_purchase, '.2f'))
    print('Total sales: ',  format(amount_purchase+state_sales_tax*amount_purchase+county_sales_tax*amount_purchase, '.2f'))
main()

#7

def main():
    number_miles=int(input('Enter miles driven: '))
    gallon=int(input('Enter gallons: '))
    print('MPG: ', format(number_miles/gallon, '.2f'))    
main()


#8

def main():
   tax=0.07
   tip=0.18
   charge_food=int(input('Enter charge for food: '))
   sales_tax=charge_food*tax
   tip=charge_food*tip
   print('Charge for food: ', charge_food)
   print('Sales tax: ', format(sales_tax, '.2f'))
   print('Tip: ', format(tip, '.2f'))
   print('Total:', format(charge_food+sales_tax+tip, '.2f'))    
main()

#9

#10

#11

#12






























