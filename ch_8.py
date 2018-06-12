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



#5



#6
#7
#8
#9
#10
#11
#12