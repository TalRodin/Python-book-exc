#chapter 2

#1

def main():
    print("Name\nAddress\nPhone Number\nCollege Major")   
main()

#2

def main():
    total_sales= input("Please, enter the total sales: ")
    print('Annual profit: $', 0.23*int(total_sales))
main()

#3

def main():
    square_feet=input("Enter the total square feet in a tract of land: ")
    print("The number of acres in the tract: ", format(int(square_feet)/43560, '.2f'))
main()

#4

def main():
    #items=5    
    #price_1=int(input("Price 1st item: "))
    #price_2=int(input("Price 2nd item: "))
    #price_3=int(input("Price 3rd item: "))
    #price_4=int(input("Price 4th item: "))
    #price_5=int(input("Price 5th item: "))
    #subtotal_cost=price_1+price_2+price_3+price_4+price_5
    price=list(map(int, input().split()))
    subtotal_cost=sum(price)    
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
#F=9/5*C+32

def main():
   C=int(input('Please enter the temperature in C: ')) 
   print("The temperature in F: ", 9/5*C+32)
main()

#10

def main():
    sugar=1.5
    butter=1
    flour=2.75
    number=48
    n=int(input("Please enter the amount of cookies you want: "))
    one_sugar=sugar/number
    one_butter=butter/number
    one_flour=flour/number
    new_sugar=n*one_sugar
    new_butter=n*one_butter
    new_flour=n*one_flour
    print('You need ', format(new_sugar, '.2f'), " cups of sugar,  ", format(new_butter,'.2f'), " cups of butter, and ", format( new_flour,'.2f'), " cups of flour.")
main()

#11

def main():
    female=int(input("Enter the number of female: "))
    male=int(input("Enter the number of male: "))
    total_students=female+male
    print("The percentage of males: ", format((male/total_students)*100,'.3f'))
    print("The percentage of females: ", format((female/total_students)*100, '.3f'))    
main()

#12

def main():
    number_stocks=2000
    per_share_price=40
    commission=0.03
    total_commission_purchased=commission*per_share_price*number_stocks
    total_purchased_cost=number_stocks*per_share_price
    total_purchased_after_commission=total_purchased_cost+total_commission_purchased
    
    
    sold=2000
    per_share_sold=42.75
    commission=0.03
    total_commission_sold=commission*per_share_sold*sold
    total_purchased_sold=number_stocks*per_share_sold
    total_sold_after_commission=total_purchased_sold-total_commission_sold
    
    print('The amount of money Joe paid for the stock-one stock: ',  per_share_price)
    print('The amount of commission Joe paid his broker when he bought the stock: ',total_commission_purchased)
    print('The amount that Joe sold the stock for: ', per_share_sold)
    print('The amount of commission Joe paid his broker when he sold the stock: ',total_commission_sold)
    print('The amount of money that Joe had left when he sold the stock and paid his broker: ',total_sold_after_commission)
    
    if total_sold_after_commission>total_purchased_after_commission:
        print("Joe made profit. " )
    else:
        print("Joe made loss. ")    
main()





























