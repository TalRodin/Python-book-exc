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

def main():
   country_capital={}
   country_capital['Russia']='Moscow'
   country_capital['USA']='WashingtonDC'
   country_capital['France']='Paris'
   country_capital['UK']='London'
   
main()


#3

#4

#5

#6

#7

#8

#9


