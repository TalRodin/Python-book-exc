# chapter 9

#1

def main():
   course_room={'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411'}
   course_instructor={'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
   course_time={'CS101':'8:00 a.m.','CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.'}
   course_number=input("Please enter the course number: ")
   for key in course_room:
       if course_number==key:
           print(course_number, course_room[key], end=' ')
   for key in course_instructor:
       if course_number==key:
           print(course_instructor[key], end=' ')       
   for key in course_time:
       if course_number==key:
           print(course_time[key], end=' ')
main()


#2

import random
def main():
    keep_going='y'
    while keep_going=='y':
        dic_countries={'Russia':'Moscow','France':'Paris','Great Britain':'London','Israel':'Jerusalem'}
        country = random.choice(list(dic_countries.keys()))
        print(country)
        capital=input()
        if capital==dic_countries[country]:
            print("Correct")
        else:
            print("Incorrect")
        
        keep_going=input("Please enter 'y' to continue: ")    
        
        
main()  

#3

def main(infile_content, codes):
     for i in infile_content:
         for key in codes:
             if i==key:
                 print(codes[key], end='')
             


if __name__ == '__main__':

   codes={'A':'%','a':'9','B':'@','b':'#','C':'!','c':'$','D':'^','d':'&','E':'2','e':'5','F':'4','f':'7','G':'0','g':'*','H':'+','h':'_','I':'66','i':'99','J':'88','j':'!~','K':'::','k':'<>','L':'<','l':'|','M':':','m':'}',
         'N':'1','n':',','O':'3','o':'.','P':'6','p':'?','Q':'/','q':'8','R':':','r':'=','S':'?','s':'~','T':'-','U':'`','V':'>','v':'{', 'W':'(','w':',','X':')','x':'[',
         'Y':']','y':'11','Z':'33','z':';'}
   infile=open('textfile_9ch.txt','r',encoding="utf-8")
   infile_content=infile.read()
   print(infile_content)
   main(infile_content, codes)



#4

def main(infile_content):
    print(infile_content)
    myset=set()
    for value in infile_content:
        myset.add(value)
    print(' '.join(myset))




if __name__ == '__main__':
    
    infile=open('text_9ch_4prob.txt', 'r', encoding="utf-8")
    infile_content=infile.read().split()
    #print(infile_content)
    main(infile_content)

#5

def main(infile_content):
    print(infile_content)
    dict_={}
    list_=[]
    for i in infile_content:
        list_.append(i)
        
    for key in infile_content:
        
        dict_[key]=list_.count(key)
    for j in dict_:
       print(j,' ', dict_[j], end='\n')



if __name__ == '__main__':
    
    infile=open('text_9ch_4prob.txt', 'r', encoding="utf-8")
    infile_content=infile.read().split()
    #print(infile_content)
    main(infile_content)


#6

def main(infile_content_1, infile_content_2):
    
    print(infile_content_1)
    print(infile_content_2)
    set_1=set()
    set_2=set()

    for value in infile_content_1:
        set_1.add(value)
    print(' '.join(set_1))
    for value in infile_content_2:
        set_2.add(value)
    print(' '.join(set_2))

    unique_words=set_1|set_2
    print('Unique words: ', unique_words)
    union_=set_1&set_2
    print("Words appear in two sets: ", union_)
    first_file_not_second=set_1-set_2
    print("Words only in first file: ",first_file_not_second )
    second_file_not_first=set_2-set_1
    print("Words only in second file: ",second_file_not_first)
    print("Words in first or second but not in both: ", unique_words- union_)

if __name__ == '__main__':
    
    infile=open('text_9ch_4prob.txt', 'r', encoding="utf-8")
    infile_content_1=infile.read().split()
    #print(infile_content)
    infile_=open('text_9ch_6prob.txt', 'r', encoding="utf-8" )
    infile_content_2=infile_.read().split()
    main(infile_content_1, infile_content_2)

#7

def main(list_):
    
    list_.pop()
    new_list=[]
    dict_={}
    print(list_)
    for _ in list_:
        print(_[-1])
        new_list.append(_[-1])
    print(new_list)
    for i in new_list:
        dict_[i]=new_list.count(i)
    print(dict_)

    your_choice(dict_)
    
def your_choice(dict_):
    choice=input("Please enter what team: ")
    if choice in dict_:
        print(dict_[choice])
    
if __name__ == '__main__':
    infile=open('WorldSeriesWinners.txt', 'r',encoding="utf-8")
    list_=[]
    infile_content=infile.readline()
    while infile.readline()!='':
        list_.append(infile_content.split())
        infile_content=infile.readline()
    #infile_content=infile.read().split('\n')
    main(list_)

#8

def main():

    print("1. Look up a person's email: ")
    print("2. Add a new name and email address: ")
    print("3. Change an existing email address: ")
    print("4. Delete an existing name and email address: ")
    choice=int(input())
    return choice


def look_up(email_addresses):
    name=input("Enter name: ")
    print(email_addresses.get(name, "Not found."))
def add(email_addresses):
    name=input("Enter name: ")
    e_address=input("Enter email address: ")
    
    if name not in email_addresses:
        email_addresses[name]=e_address
    else:
        print('This name exists.')
        
        
        
def change(email_addresses):
    name=input("Enter the name: ")
    if name in email_addresses:
        email=input("Enter the new email: ")
        email_addresses[name]=email
    
    else:
        print("That name is not found.")
        
def delete(email_addresses):
    
    name=input("Enter the name: ")
    if name in email_addresses:
        del email_addresses[name]
    else:
        print("That name is not found.") 

if __name__=='__main__':
    
    LOOK_UP=1
    ADD=2
    CHANGE=3
    DELETE=4
    QUIT=5
    
    email_addresses={}
    
    choice=0
    
    while choice!=QUIT:
        
        choice=main()
        
        if choice==LOOK_UP:
            look_up(email_addresses)
        elif choice==ADD:
            add(email_addresses)
        elif choice==CHANGE:
            change(email_addresses)
        elif choice==DELETE:
            delete(email_addresses)

#9


