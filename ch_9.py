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





#4

#5

#6

#7

#8

#9


