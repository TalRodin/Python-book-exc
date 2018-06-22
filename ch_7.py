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

def main():
    infile=open('USPopulation.txt', 'r')
    list_=[]
    list_change=[]
    
    infile_content=infile.readline()
    while infile_content!='':
        list_.append(infile_content.split())
        infile_content=infile.readline()
        
    print(list_)   
    del list_[0]
    i=1
    for i in range(len(list_)):
        change=int(list_[i][1])-int(list_[i-1][1])
        list_change.append(change)
    print(list_change)
    del list_change[0]
    list_change.insert(0,0)
    print(list_change)
    total=0
    
    for value in list_change:
        total+=int(value)
    
    print("The average change: ",format(total/len(list_change), '.2f'))
    
    maxC=0
    minC=0
    change=1
    for change in range(len(list_change)):
        if list_change[change]>list_change[change-1]:
            minC=maxC
            maxC=list_change[change]
            year=list_[change][0]
    print('Max change year: ', maxC, end=' ')
    print(year)
    print(min(list_change[1:]))
    print(list_change.index(min(list_change[1:])))
    print('Min change year: ', list_[list_change.index(min(list_change[1:]))][0])
    
main()


#10

def main():
    infile=open('WorldSeriesWinners.txt','r')
    infile_content=infile.readline()
    list_teams=[]
    while infile_content!='':
        list_teams.append(infile_content.split())
        infile_content=infile.readline()
    #print(list_teams)
    new_list_team=[]
    
    for i in list_teams:
            print(i[-1])
            new_list_team.append(i[-1])
    print(new_list_team)
    aTeam=input()
    total=new_list_team.count(aTeam)
    print(total)
    count=0
    for team in new_list_team:
        if aTeam==team:
            count+=1
    print(count)   
    
main()

#11

def main():
    rows=3
    columns=3
    values=[[0]*columns,
            [0]*columns,
            [0]*columns]
    
    
    for i in range(rows):
        for j in range(columns):
            values[i][j]=int(input())
    a, b=test_Lo_Shu(values)
    
    if a==b:
        print("Magic Square")
    else:
        print("Try again")
    print(values)
def test_Lo_Shu(values)    :
    
    list_sum_rows=[]
    for i in values:
        list_sum_rows.append(sum(i))
        
    print(list_sum_rows)
    list_=[]
    total_1=0
    total_2=0
    total_3=0
    for i in range(len(values)):
       total_1+=values[i][0]
       total_2+=values[i][1]
       total_3+=values[i][2]
   
       
    list_.insert(0,total_1)    
    list_.insert(1,total_2)
    list_.insert(2,total_3)   
        
    
    
    return(list_, list_sum_rows)  
        
        
main()

