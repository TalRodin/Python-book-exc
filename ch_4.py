#1

def main():
    number_days=5
    total_bugs=0
    for i in range(number_days):
        bugs=int(input("Enter number of bugs: "))
        total_bugs+=bugs
    print('\n', total_bugs)
main()

#2

def main():
    burn_cal=4.2
    for i in range (10,30+5, 5):
        print('\nBurned cal: ', i*burn_cal)
main()

#3

def main():
    total_exp=0
    num_days_month=int(input('Enter number days a month: '))
    for i in range (1,num_days_month+1,1):
        exp=int(input('Enter expenses: '))
        total_exp+=exp
    print("Total expenses for the month: ",total_exp )
main()

#4

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

#7

#8



#9

def main():
   rise=1.6
   n=25
   for y in range(n):
       rise+=rise
       print(rise)
main()

#10

def main():
    tuition=8000
    percent=0.03
    n=5
    t=1
    for t in range (n+1):
        tuition=tuition+(tuition*percent)
        print('\n',t,' ',tuition)
main()

#11

def main():
    number=int(input("Please enter the number: "))
    f=1
    for n in range (number,1,-1):
        f*=n      
    print(f," is a factorial of ", number)
main()

#12
#13
#14
