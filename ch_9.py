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



#8

#9


