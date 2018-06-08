#chapter 6

#1

print('--'*10)
def main():
  file=open('numbers.txt','r') 
  file_content=file.read()
  file.close()  
  print(file_content)
main()

#2

print('--'*10)
def main():
   file=input("Please enter the name of the file: ")
   infile=open(file, 'r',encoding="utf-8")
   line1=infile.readline()
   line2=infile.readline()
   line3=infile.readline()
   line4=infile.readline()
   line5=infile.readline()
   infile.close()   
   print('\n',line1,'\n',line2,'\n',line3,'\n',line4,'\n',line5)
main()

#3

print('--'*10)
def main():
   file=input("Please enter the name of the file: ")
   infile=open(file, 'r',encoding="utf-8")
   n=1
   for line in infile:      
       print(n,': ',line)
       n+=1
   infile.close() 
main()

#4

print('--'*10)
def main():
    infile=open('names.txt', 'r', encoding="utf-8")
    count=0
    for line in infile:
        count+=1
    print("Total number of names: ", count)
    infile.close()
main()

#5

print('--'*10)
def main():
   infile=open("numbers.txt", 'r')
   infile_content=infile.read().split(' ')
   print (infile_content)
   total=0
   for i in infile_content:
       total+=int(i)
   print(total)  
   infile.close()   
main()

#6

print('--'*10)
def main():
   infile=open("numbers.txt", 'r')
   infile_content=infile.read().split(' ')
   print (infile_content)
   total=0
   count=0
   for i in infile_content:
       total+=int(i)
       count+=1
   print(total)
   print(count)
   average(total, count) 
   infile.close()
def average(total,c):
    average=total/c
    print(average)
main()


#7

print('--'*10)
import random
def main():
   outfile=open('number.txt','w')
   number_write=int(input("Please enter the number to write into the file: "))
   for i in range(number_write):
       random_number=random.randint(1,500)
       outfile.write(str(random_number)+'')
   outfile.close()
main()

#8

print('--'*10)
def main():
   infile=open('number.txt', 'r')
   infile_content=infile.readline()  
   total=0
   count=0   
   while infile_content!='':
       f=float(infile_content)

       total+=int(f)
       count+=1
       infile_content=infile.readline()
   print(total)
   print(count)
   infile.close()    
main()

#9

print('--'*10)


#10

print('--'*10)
