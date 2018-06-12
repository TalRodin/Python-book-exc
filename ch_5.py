#chapter 5

import random

#1

print('--'*10)
def main():
   kilometers=int(input("Please enter the distance in kilometers: "))
   miles=kilometers*0.6214
   print("Miles: ", miles)
main()

#2

print('--'*10)
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

print('--'*10)
def main():
   cost_replace_structure=int(input("Please enter the replacement cost: "))
   ins=0.80
   print("Minimum amount of insurance to buy: ", ins*cost_replace_structure)
main()

#4

print('--'*10)
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
print('--'*10)


#6

print('--'*10)
def main():
   fat=int(input("Please enter amount of fat: "))
   carb=int(input("Please enter amount of carb: "))
   fat_(fat)
   carb_(carb)
def fat_(fat):
    print("Calories from fat: ", fat*9)
def carb_(carb):
    print("Calories from carb: ", carb*4)
main()

#7

print('--'*10)
def main():
    A=int(input("Please enter amount of A tickets: "))
    B=int(input("Please enter amount of B tickets: "))
    C=int(input("Please enter amount of c tickets: "))
    calc(A,B,C)    
def calc(A,B,C):
    print("Total income: ", A*20+B*15+C*10)
main()

#8

print('--'*10)



#9

print('--'*10)
def main():
    total_sales=int(input("Please enter the total sales: "))
    c=county_tax(total_sales)
    print("County tax: ", c)
    s=state_tax(total_sales)
    print("State tax ", s)
    total_sales_tax(c,s)
def county_tax(total_sales):
    c=0.025*total_sales
    return (c)
def state_tax(total_sales):
    s=0.05*total_sales
    return (s)
def total_sales_tax(c,s):
    print("Total sales taxes: ", c+s)    
main()

#10

print('--'*10)
def main():
    #1foot=12inches
    number=int(input("Please enter the number of feet: "))
    inches(number)   
def inches(number):
    print("Inches: ", 12*number)    
main()

#11

print('--'*10)
def main():
    choice=int(input("Please enter the level of the game (1,2,3): "))
    if choice ==1:
            r=10
            game_1(r)
    elif choice== 2:
            r=20
            game_2(r)
    elif choice== 3:
            r=30
            game_3(r)
    else:
        print("Error")
def game_1(r):    
    number_1=random.randint(1,r)
    number_2=random.randint(1,r)
    total=number_1+number_2
    ans=int(input("Please enter your answer: "))
    if ans==total:
        print("Correct!")
    else:
        print("Incorrect...")
def game_2(r):    
    number_1=random.randint(1,r)
    number_2=random.randint(1,r)
    total=number_1+number_2
    ans=int(input("Please enter your answer: "))
    if ans==total:
        print("Correct!")
    else:
        print("Incorrect...")
def game_3(r): 
    number_1=random.randint(1,r)
    number_2=random.randint(1,r)
    total=number_1+number_2
    ans=int(input("Please enter your answer: "))
    if ans==total:
        print("Correct!")
    else:
        print("Incorrect...")
main()

#12

print('--'*10)
def main():
    int_1=int(input("Please enter the first integer: "))
    int_2=int(input("Please enter the second integer: "))
    comp(int_1, int_2)    
def comp(int_1, int_2):
    if int_1>int_2:
        print(int_1)
    else:
        print(int_2)
main()

#13

print('--'*10)
g=9.8
def main():
    time=int(input("Please enter the time in seconds: "))
    for t in range (1,time+1,+1):
        d=dist(t)
        print(t,' '*5, d)
def dist(t):
    d=1/2*g*(t**2)
    return d
main()

#14

print('--'*10) 
def main():   
    m=int(input("Please enter the mass: "))
    v=int(input("Please enter the velocity: "))
    KE(m,v)
def KE(m,v):
    KE=1/2*m*(v**2)
    print("KE:", KE)
main()

#15

print('--'*10)
def main():
    list_=[]
    for i in range(5):
        score=int(input("Please enter the score: "))
        list_.append(score)
    a=calc_average(list_)
    print("Average: ",a)
    determine_grade(a)
def calc_average(list_):   
    total=0
    for i in list_:
        total+=int(i)
    average=total/5
    return (average) 
def determine_grade(a):
    if 90<=a<=100   :
        print("Grade: A")
    elif 80<=a<=89   :
        print("Grade: B")
    elif 70<=a<=79   :
        print("Grade: C")
    elif 60<=a<=69   :
        print("Grade: D")
    elif a<60   :
        print("Grade: F")
main()

#16

print('--'*10)
def main():
    odd_total=0
    even_total=0
    for i in range(1,100):
        number=random.randint(1,100)
        if number%2==0:
            even_total+=1
        else:
            odd_total+=1
    print("Odd total: ", odd_total)
    print("Even total: ", even_total)    
main()

#17

print('--'*10)
def main():
    number=int(input("Please enter the number: "))
    print(prime(number))
def prime(number):
    for i in range(2,number):
        if not number%i:
            return False
    return True  
main()

#18

print('--'*10)
def main():
    number=int(input("Please enter the number: "))
    for i in range (number):
        if prime(i)==True:
            print(i)        
def prime(number):
    for i in range(2, number):
        if not number%i:
            return False
    return True
main()

#19

print('--'*10)
def main():
    present_value=int(input("Please enter the present value: "))
    monthly_interest_rate=int(input("Please enter the monthly interest rate:"))
    number_month=int(input("Number of months: "))
    amount(present_value,monthly_interest_rate,number_month)
    
def amount(present_value,monthly_interest_rate,number_month):
    F=present_value*(1+monthly_interest_rate/100)**number_month
    print(format(F, '.2f'))
main()

#20

print('--'*10)
def main():
    number=random.randint(1,100)
    guess=int(input())
    if number>guess:
        print("Too high, try again.")
    elif number<guess:
        print("Too low, try again.")
    else:
        print("Correct.")
main()

#21

print('--'*10)
def main():
   number=random.randint(1,3) 
   choice=''
   if number==1:
       choice='rock'
   elif number==2:
       choice='paper'
   else:
       choice='scissors'
       
   user_choice=input()
   print(choice)
   if user_choice=='rock' and  choice=='scissors':
       print("User won")
   elif user_choice=='scissors' and  choice=='rock':
       print("Computer won")
   elif user_choice=='scissors' and  choice=='paper':
       print("User won")
   elif user_choice=='paper' and  choice=='scissors':
       print("Computer won")
   elif user_choice=='paper' and  choice=='rock':
       print("User won")
   elif user_choice=='rock' and  choice=='paper':
       print("Computer won")
   else:
       'Error'
main()




















