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
   print("Weight: ",weight)
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
        print("Purple")
    elif (first_color=='yellow' and second_color=='blue') or (first_color=='blue' and second_color=='yellow'):
        print("Purple")
    else:
        print("Error")
    
main()

#8

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


#11
#12
#13
#14
#15


























