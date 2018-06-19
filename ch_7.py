#chapter 7

#1

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

def main():
    outfile=open ('charge_accounts.txt', 'w')    
    for i in range (5):
        accounts=int(input("Enter charge account: "))
        outfile.write(str(accounts)+'\n')        
    outfile.close()
    print(outfile)    
main()
    
def account_validation():
    list_=[]
    file=open('charge_accounts.txt','r') 
    file_content=file.read().split('\n')
    print(file_content)
    for i in file_content:
        print(i)
        list_.append(i)
    print(list_)
    file.close()  
    #print(file_content)
    list_.remove('')
    print(list_)
    user_account=input("Enter your account to validate: ")
    for i in range(len(list_)):
        if list_[i] ==user_account:
            print("Valid")
        else:
            False            
account_validation()

#6

def main():
    list_=[1,2,3,4,5,6,7,8]
    n=int(input())
    for i in range(len(list_)):
        if n<list_[i]:
            print(list_[i])
main()

#7

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

def main():
    infile_girls=open("GirlNames.txt", 'r') 
    infile_boys=open("BoyNames.txt", 'r')
    girl_file_content=infile_girls.read()
    boy_file_content=infile_boys.read()
    print(girl_file_content)
    print(boy_file_content)
    name=input()
    if name in girl_file_content or name in boy_file_content:        
        print("Popular")
    else:
        print("Not popular")
main()

#9



#10

#11



