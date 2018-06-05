#1

def main():
  file=open('numbers.txt','r') 
  file_content=file.read()
  file.close()  
  print(file_content)
main()

#2

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


#5
#6
#7
#8
#9
#10

