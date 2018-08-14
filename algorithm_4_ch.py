#1

def main():
   num=int(input())   
   num*=10
   product=num
   while (product<100):
       num=int(input())   
       num*=10
       product=num       
main()

#2


def main():
    keep_going='y'
    while keep_going=='y':
        num1=int(input())
        num2=int(input())
        total=num2+num1
        print(total)
        keep_going=input(" 'y' for continue: ")               
main()

#3


def main():
    for i in range(1000+1):
        print(i)
main()

#4


def main():   
    total=0
    i=0
    while (i<10):
        num=int(input())
        total+=num
        i+=1
    print(total)
main()

#5


def main():   
   total=0
   for numerator in range(1,30,1):
       for denominator in range(30,1,-1):
           total+=numerator/denominator
   print(total)        
main()

#6

x+=1
x*=2
x/=10
x-=100

#7

def main():
   row=10
   col=15
   for i in range(row):
       for j in range(col):
           print('#', end='')
       print()
main()

#8


def main():
       keep_going='y'
       while (keep_going=='y'):
           pos_num=int(input("Positive number: "))
           if pos_num>=1:
               print(pos_num)
           else:
               print("Error")
           keep_going=input("'y' to continue: ")           
main()

#9


def main():
       keep_going='y'
       while (keep_going=='y'):
           pos_num=int(input("Positive number from 1 to 100: "))
           if pos_num>=1 and pos_num<=100:
               print(pos_num)
           else:
               print("Error")
           keep_going=input("'y' to continue: ")           
main()
