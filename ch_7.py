 #chapter 7

#1

print('--'*10)
def main():
  sales=[]
  for i in range(7):
      s=int(input("Enter the sales for the day: "))
      sales.append(s)
  print(sales)
  total=0
  for s in sales:
      total+=int(s)
  print("Total sales: ", total)
main()

#2

print('--'*10)
import random
def main():
   random_list=[]
   for i in range (7):
       random_number=random.randint(0,9)
       random_list.append(random_number)
   for number in random_list:
       print(number)
main()

#3

print('--'*10)
def main():
   rain=[]
   for r in range(12):
       rainfall=int(input("Please enter the rainfall for the month: "))
       rain.append(rainfall)
   total=0
   for r in rain:
       total+=int(r)
   print("Total rainfall for the year: ", total )
   print("Average: ", format(total/12, '.2f'))
   print("Max: ", max(rain))
   print("Min: ", min(rain)) 
main()

#4

print('--'*10)
def main():
   numbers=[]
   for n in range(20):
       num=int(input("Please enter the numbers: "))
       numbers.append(num)
   print(numbers)
   print("The lowest number in the list: ", min(numbers))
   print("The highest number in the list: ", max(numbers))
   total=0
   for n in numbers:
       total+=int(n)
   print("The total numbers in the list: ",total )
   print("The average: ", total/20)
main()

#5


#6

print('--'*10)
def main():
    list_=[1,2,3,4,5,6,7,8]
    n=int(input())
    for i in range(len(list_)):
        if n<list_[i]:
            print(list_[i])
main()

#7

print('--'*10)

def main():
    correct_answer=['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','A','B','B','D','A']
    student=[]
    
    for i in range(20):        
        student_answer=input()
        student.append(student_answer)
        
    print(correct_answer) 
    print(student)
    if student==correct_answer:
        print("Passed")
    else:
        print("Not passed")
    count_correct=0
    count_incorrect=0
    for value in range(len(correct_answer)):
       if correct_answer[value]!=student[value]:
           count_correct+=1
       else:
           count_incorrect+=1            
    print(count_correct)
    print(count_incorrect)
main()

#8
print('--'*10)


#9
print('--'*10)
#10
print('--'*10)
#11
print('--'*10)


