#1

def main():
   kilometers=int(input("Please enter the distance in kilometers: "))
   miles=kilometers*0.6214
   print("Miles: ", miles)
main()

#2

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

#3

def main():
   cost_replace_structure=int(input("Please enter the replacement cost: "))
   ins=0.80
   print("Minimum amount of insurance to buy: ", ins*cost_replace_structure)
main()

#4

def main():
    #monthly
   loan_payment=int(input("Loan: "))
   insurance=int(input("Insurance: "))
   gas=int(input("Gas: "))
   oil=int(input("Oil: "))
   tires=int(input("Tires: "))
   maintenance=int(input("Maintenance: "))
   total_monthly_costs=loan_payment+insurance+gas+oil+tires+maintenance
   print("\nTotal monthly costs: ", total_monthly_costs)
   print("Total yearly costs: ", total_monthly_costs*12)    
main()

#5


#6
#7
#8
#9
#10
#11

#12
#13

#14
 
def main():   
    m=int(input("Please enter the mass: "))
    v=int(input("Please enter the velocity: "))
    KE(m,v)
def KE(m,v):
    KE=1/2*m*(v**2)
    print("KE:", KE)
main()
