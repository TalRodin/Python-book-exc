#1

def main():
    number_days=5
    total_bugs=0
    for i in range(number_days):
        bugs=int(input("Enter number of bugs: "))
        total_bugs+=bugs
    print(total_bugs)
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
#14