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

print('--'*10)
def main():    
    outfile=open('code.txt', 'w')  
    for i in range(5):
        c=int(input("Please enter the code: "))
        outfile_content=outfile.write(c)
        print(outfile_content)
    outfile.close()
    open_file(outfile)

def open_file(outfile):
    codes=[]
    infile=open(outfile, 'r')
    for i in range(5):
        infile_content=infile.readline()
        codes.append(infile_content)
    user(codes)    
def user(codes):
    c=input("Please enter the code: ")
    for value in codes:
        if value == c:
            print("Valid")
        else:
            print("Not valid")
main()

#6

print('--'*10)


#7

print('--'*10)


#8
print('--'*10)
#9
print('--'*10)
#10
print('--'*10)
#11
print('--'*10)


