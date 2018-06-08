#chapter 4

#1

print('--'*10)
def main():
    number_days=5
    total_bugs=0
    for i in range(number_days):
        bugs=int(input("Enter number of bugs: "))
        total_bugs+=bugs
    print('\n', total_bugs)
main()

#2

print('--'*10)
def main():
    burn_cal=4.2
    for i in range (10,30+5, 5):
        print('\nBurned cal: ', i*burn_cal)
main()

#3

print('--'*10)
def main():
    total_exp=0
    num_days_month=int(input('Enter number days a month: '))
    for i in range (1,num_days_month+1,1):
        exp=int(input('Enter expenses: '))
        total_exp+=exp
    print("Total expenses for the month: ",total_exp )
main()

#4

print('--'*10)
#distance=speed*time
def main():
    speed=int(input("Enter the speed: "))
    hours=int(input("Enter the hours it traveled: "))
    print("Hour",' '*10, "Distance traveled")
    print("--------------------------------")
    for i in range(1,hours+1, 1):
        distance=speed*i
        print(i,' '*10,distance)
main()

#5

print('--'*10)
def main():
    n_years=int(input("Please enter the number of years: "))
    month=12
    total=0
    for n in range(n_years):
        for m in range(month):
            inch=int(input("Please enter number of inches for the month: "))
            total+=inch
    print("Number of months: ", month*n_years)
    print("Total inches of rainfall: ",total)
    print("Average: ", format(total/(month*n_years), '.2f'))
main()

#6

print('--'*10)
def main():
   #F=9/5*C+32
   for C in range(0,20,1):
       F=9/5*C+32
       print(C ,'\u00B0C =',format( F, '.2f'), '\u00B0F')
main()

#7

print('--'*10)
def main():
   number_days=int(input("Please enter the number of days: "))
   print('Day: ', ' '*10, 'Salary: ')
   print('-------------------------')
   total=0.01
   print('1',' '*15, '$ 0.01')
   for d in range(1,number_days,1):
       d+=1
       total*=2
       print(d, ' '*15, '$',total)
main()

#8

print('--'*10)
def main():
  number= int(input("Please enter the number: "))
  total=0
  while number>-1:
      total+=number
      number=int(input("Please enter next number: "))
  print ("Total: ", total)    
main()


#9

print('--'*10)
def main():
   rise=1.6
   n=25
   y=1
   print(y,' '* 10 , rise )
   for y in range(1,n,1):
       y+=1
       rise+=rise
       print(y, ' '* 10 , rise)
main()

#10

print('--'*10)
def main():
    tuition=8000
    percent=0.03
    n=5
    t=1
    print(' 0', ' ', tuition)
    for t in range (1,n+1,1):
        tuition=tuition+(tuition*percent)
        print('\n',t,' ',format(tuition, '.2f'))
main()

#11

print('--'*10)
def main():
    number=int(input("Please enter the number: "))
    f=1
    for n in range (number,1,-1):
        f*=n      
    print(f," is a factorial of ", number)
main()

#12

print('--'*10)
def main():
   starting_number=int(input("Please enter the starting number of organisms: "))
   average_increase=int(input("Please enter the average increase (%): "))
   number_days=int(input("Please enter the number of days: "))   
   print('1',' '*10, starting_number)
   for d in range (1,number_days,1):
       d+=1
       increase_percent=average_increase/100
       increase=increase_percent*starting_number
       starting_number+=increase
       print(d, ' '*10, format( starting_number, '.5f')) 
main()

#13

print('--'*10)
def main():
    base_size=7
    for row in range(base_size):
        for col in range(base_size-row):
            print('*',end=' ')
        print()               
main()

#14

print('--'*10)
def main():
     base_size=6
     for row in range(base_size):
         print('#', end='', sep='')
         for spaces in range(row):            
                 print(' ', end='', sep='')
         print('#', sep=' ')
main()
































