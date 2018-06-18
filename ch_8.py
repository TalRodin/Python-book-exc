#chapter 8

#1

def main():
   name=input("Please enter your name: ")
   name.split(' ')
   for n in name:
       print(n[0])
main()

#2

def main():
   number=input("Please enter the number: ")
   total=0
   for n in number:
       total+=n
   print(total)
main()

#3

def main():
    date=input("Please enter the date in format mm/dd/yyyy: ")    
    date=[]
    date.append(date.split('/'))
    if date[0]=='01':
        m='January'
    elif date[0]=='02':
        m='February'
    elif date[0]=='03':
        m='March'
    elif date[0]=='04':
        m='April'
    elif date[0]=='05':
        m='May'
    elif date[0]=='06':
        m='June'
    elif date[0]=='07':
        m='July'
    elif date[0]=='08':
        m='August'
    elif date[0]=='09':
        m='September'
    elif date[0]=='10':
        m='October'
    elif date[0]=='11':
        m='November'
    elif date[0]=='12':
        m='December'
    else:
        print("Error")       
    print (m,' ', date[1], ', ', date[3] )
main()

#4

def main():
   aString=input()
   list_1=[' ',',','.','?','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
   list_2=[' ','--..--','.-.-.-','.-.-.-','..--..','-----','.----','..----','...--','....-','.....','-....','--...','---..','----.','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.-','--..']
   list_3=[]  
   for i in aString:
       i=i.upper()
       list_3.append(i)       
   print(list_3)           
   for i in list_3:       
           l=list_1.index(i)           
           print(list_2[l], end=' ')         
main()

#5

def main():    
    list_1=[]
    list_2=[]
    number=input("Please enter phone number: ")
    print(number)
    for i in number:
        list_1.append(i)
    print(list_1)
    for i in range(3,len(list_1)):
        if list_1[i]=='A' or  list_1[i]=='B' or list_1[i]=='C':
            list_2.append('2')
        elif list_1[i]=='D' or list_1[i]== 'E' or list_1[i]== 'F':
            list_2.append('3')
        elif list_1[i]=='G' or list_1[i]=='H' or list_1[i]=='I':
            list_2.append('4')
        elif list_1[i]=='J' or list_1[i]=='K' or list_1[i]=='L':
            list_2.append('5')
        elif list_1[i]=='M' or list_1[i]=='N' or list_1[i]=='O':
            list_2.append('6')
        elif list_1[i]=='P' or list_1[i]=='Q' or list_1[i]=='R' or list_1[i]=='S':
            list_2.append('7')
        elif list_1[i]=='T' or list_1[i]=='U' or list_1[i]=='V':
            list_2.append('8')
        elif list_1[i]=='W' or list_1[i]=='X' or list_1[i]=='Y'or list_1[i]=='Z':
            list_2.append('9')
        elif list_1[i]=='-':
            list_2.append('-')
        else:
            print("Error")
    new_phone=list_1[:3]+list_2[:]
    print(''.join(new_phone))
main()

#6

def main():
    infile=open('text.txt', 'r')
    infile_content=infile.read()
    count=0
    for line in infile_content:
        for word in line:
            count+=1
        print(count)        
    infile.close()
main()



#7

def main():
    infile=open('text.txt', 'r', encoding="utf-8")
    infile_content=infile.read()
    lCase=0
    uCase=0
    digits=0
    whitespace=0
    for i in infile_content:
        if i.isdigit():
            digits+=1
        elif i==' ':
            whitespace+=1
        elif i.isupper():
            uCase+=1
        elif i.islower():
            lCase+=1
    print(digits)
    print(whitespace)
    print(uCase)
    print(lCase)    
    infile.close()
main()

#8

def main():
    aString=input()
    print(aString.title())
main()

#9

def main():
   aString=input()   
   vowels_(aString)
   consonants_(aString)
def vowels_(aString):
       vowels=['a','e','i','o','u','y']
       count=0
       for i in aString:
           if i in vowels:
               count+=1
       print(count)
def consonants_(aString):
       consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
       count=0
       for i in aString:
           if i in consonants:
               count+=1
       print(count)   
main()

#10

def main():
    aString=input()
    list_=[]
    #a=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z','a','e','i','o','u','y']
    maxV=0
    minV=0
    maxV_=''
    a=aString.lower()
    for i in a:
        q=a.count(i)
        if q>maxV and i.isalpha():
            minV=maxV
            maxV=q
            maxV_=i   
    print(maxV_)
    print(maxV)                
main()

#11

def main():
    list_=[]    
    aString=input()
    ch=' '
    for i in aString:         
         if i.isupper():
             ch_i=ch+i.lower()
             print( ch_i, end='')
             list_.append(ch_i)
         else:
             print(i, end='')
             list_.append(i)
    print(list_)       
    print(aString[0]+''.join(list_[1:]))      
main()

#12

def main():
    aString=input()   
    a=aString.split(' ')
    for word in a:
       b=word[1:]+word[0]+'AY'
       print(b,end=' ')
main()

