#chapter 3

#1

def main():
    number = int(input("Enter the number from 1 to 7: "))
    if number == 1:
        print('Monday')
    elif number == 2:
        print('Tuesday')
    elif number == 3:
        print('Wednesday')
    elif number ==4 :
        print('Thursday')
    elif number ==5:
        print('Friday')
    elif number == 6:
        print('Saturday')
    elif number == 7:
        print('Sunday')
    else:
        print('Error')
main()

#2

def main():
    length_1=int(input("Enter the length of first rectangle: "))
    width_1=int(input("Enter the width of first rectangle: "))
    
    length_2=int(input("Enter the length of second rectangle: "))
    width_2=int(input("Enter the width of second rectangle: "))
    
    rec_1=length_1*width_1
    rec_2=length_2*width_2
    
    if rec_1>rec_2:
        print('Rectangle 1 greater rectangle 2')
    elif rec_2>rec_1:
        print('Rectangle 2 greater rectangle 1')
    else:
        print('Rectangles are equal')
main()

#3

def main():
    age=int(input('Enter your age: '))
    if age<=1:
        print('Infant')
    elif 1<age<13:
        print('Child')
    elif 13==age<20:
        print('Teenager')
    elif age>=20:
        print('Adult')
    else:
        print('Error')
main()

#4

def main():
    number=int(input('Enter the number: '))
    if number==1:
        print('I')
    elif number == 2:
        print('II')
    elif number ==3:
        print('III')
    elif number == 4:
        print('IV')
    elif number ==5:
        print('V')
    elif number ==6:
        print('VI')
    elif number ==7:
        print('VII')
    elif number==8:
        print('VIII')
    elif number==9:
        print('IX')
    elif number==10:
        print('X')
    else:
        print('Error')    
main()

#5

def main():
   mass=int(input("Enter the amount of mass of an object in kilograms: "))
   weight=mass*9.8
   print("Weight: ",format(weight, '.2f'))
   if weight<100:
       print("Too light!")
   else:
       print("Heavy.")
main()

#6


def main():
   month=int(input("Please enter the month: "))
   day=int(input("Please enter the day: "))
   year=int(input("Please enter the year: "))
   
   if month*day==year:
       print("Magic!")
   else:
       print("Not magic!")
main()

#7

def main():
    first_color=input("Please enter the first color: ")
    second_color=input("Please enter the second color: ")
    
    if (first_color=='red' and second_color=='blue') or (first_color=='blue' and second_color=='red'):
        print("Purple")
    elif (first_color=='red' and second_color=='yellow') or (first_color=='yellow' and second_color=='red'):
        print("Orange")
    elif (first_color=='yellow' and second_color=='blue') or (first_color=='blue' and second_color=='yellow'):
        print("Green")
    else:
        print("Error")
    
main()

#8

import numpy as np
def main():
    number_people=int(input("Enter number of people: "))
    number_hot_dogs=int(input("Enter number hot dogs given to each person: "))
    total_hot_dogs_needed=number_people*number_hot_dogs
    total_hot_dogs_bread=2*total_hot_dogs_needed
    
    print("Minimum number of hot dogs: ",total_hot_dogs_needed )
    print("Minimum number of hot dogs buns: ",total_hot_dogs_bread )
    print("Minimum number of packages of hot dogs: ", total_hot_dogs_needed/10)
    print("Minimum number of packages of hot dogs buns: ", total_hot_dogs_bread/8)
    if total_hot_dogs_needed/10!=0:
        left_hot_dogs=np.ceil(total_hot_dogs_needed/10)-(total_hot_dogs_needed/10)
        
    if total_hot_dogs_bread /8!=0:
        left_buns=np.ceil(total_hot_dogs_bread/8)-(total_hot_dogs_bread/8)
    print("Number of hot dogs that will left over: ",format(left_hot_dogs,'.2f'))
    print("Number of hot dogs buns that will left over: ", format(left_buns, '.2f'))
main()

#9

def main():
   number=int(input("Please enter the pocket number: "))
   if number==0:
       print("Green")
   elif 1<=number<=10:
       if number%2!=0:
           print("Red")
       else:
           print("Black")
   elif 11<=number<=18:
       if number%2!=0:
           print("Black")
       else:
           print("Red")
   elif 19<=number<=28:
       if number%2!=0:
           print("Red")
       else:
           print("Black")
   elif 29<=number<=36:
       if number%2!=0:
           print("Black")
       else:
           print("Red")
   else:
       print("Error:")
main()

#10

def main():
   #pennies 1
   #nickels 5
   #dimes 10
   #quarters 25
   #dollar 100
   number_pennies=int(input("Please enter number of pennies to make $1: "))
   number_nickels=int(input("Please enter number of nickels to make $1: "))
   number_dimes=int(input("Please enter number of dimes to make $1: "))
   number_quarters=int(input("Please enter number of quarters to make $1: "))
   
   total_pennies=number_pennies*1
   total_nickels=number_nickels*5
   total_dimes=number_dimes*10
   total_quarters=number_quarters*25

   dollar=total_pennies+total_nickels+total_dimes+total_quarters
   if dollar == 100:
       print("Dollar!")
   elif dollar<100:
       print("Less one dollar")
   elif dollar>100:
       print("More one dollar")
   else:
       print("Error")
main()
       
#11

print('--'*10)
def main():
    number_books=int(input("Please enter the number of books: "))
    if number_books==0:
        print("Number of points: ", 0)
    elif number_books==2:
        print("Number of points: ", 5)
    elif number_books==4:
        print("Number of points: ", 15)
    elif number_books==6:
        print("Number of points: ", 30)
    elif number_books==8:
        print("Number of points: ", 60)
    else:
        print("Error: ")
main()

#12

def main():
    price=99
    number_packages=int(input("Please enter the number of packages: "))
    if 10<=number_packages<=19:
        discount=0.10
    elif 20<=number_packages<=49:
        discount=0.20
    elif 50<=number_packages<=99:
        discount=0.30
    elif number_packages>100:
        discount=0.40
    else:
        print("Error: ")
    print("Total amount of purchase: ", price-(price*discount))   
main()

#13

print('--'*10)
def main():
    weight=int(input("Please enter the weight:"))
    if weight<=2:
        print("Rate: 1.50")
    elif 2<weight<=6:
        print("Rate: 3.00")
    elif 6<weight<=10:
        print("Rate: 4.00")
    elif weight>10:
        print("Rate: 4.75")
    else:
        print("Error")
main()

#14

#BMI=weight*(703/height^2)
def main():
    weight=int(input("Please enter the weight: "))
    height=int(input("Please enter the height: "))
    BMI=weight*703/(height**2)
    if 18.5<BMI<2.5:
        print("The weight is optimal")
    elif BMI<18.5:
        print("Underweight")
    elif BMI>25:
        print("Overweight")
    else:
        print("Error")
main()

#15

print('--'*10)
def main():
   number_seconds=int(input("Please enter the number of the seconds: "))
   if number_seconds>=60:
       minutes=number_seconds/60
       print("Minutes: ", minutes)
   elif number_seconds>=3600:
       hours=number_seconds/3600
       print("Hours: ", hours) 
   elif number_seconds>=86400:
       days=number_seconds/86400
       print("Days: ",days)
   else:
       print("Seconds: ", number_seconds)
main()
























