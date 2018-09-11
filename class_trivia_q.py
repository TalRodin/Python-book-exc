import random
class Question:
   def __init__(self, trivia_question, possible_answer_1, possible_answer_2, possible_answer_3, possible_answer_4, numb_corr):
        self.__trivia_question=trivia_question
        self.__possible_answer_1=possible_answer_1
        self.__possible_answer_2=possible_answer_2
        self.__possible_answer_3=possible_answer_3
        self.__possible_answer_4=possible_answer_4
        self.__numb_corr=numb_corr
        
   def set_trivia_question(self,trivia_question):
       self.__trivia_question=trivia_question
   def set_possible_answer_1(self, possible_answer_1):    
       self.__possible_answer_1=possible_answer_1
   def set_possible_answer_2(self, possible_answer_2):
       self.__possible_answer_2=possible_answer_2
   def set_possible_answer_3(self, possible_answer_3):    
       self.__possible_answer_3=possible_answer_3
   def set_possible_answer_4(self, possible_answer_4):
       self.__possible_answer_4=possible_answer_4
   def set_numb_corr(self, numb_corr):    
       self.__numb_corr=numb_corr
       
   def get_trivia_question(self):
       return self.__trivia_question
   def get_possible_answer_1(self):
       return self.__possible_answer_1
   def get_possible_answer_2(self):
       return self.__possible_answer_2
   def get_possible_answer_3(self): 
       return self.__possible_answer_3
   def get_possible_answer_4(self): 
       return self.__possible_answer_4
   def get_numb_corr(self): 
       return self.__numb_corr
   
def main():
    q_1=Question("2+2=","1. 4","2. 3","3. 8","4. 0",1)
    q_2=Question("3+9=","1. 2","2. 12","3. 4","4. 9",2)
    q_3=Question("4+6=","1. 10","2. 4","3. 9","4. 8",1)
    q_4=Question("3+7=","1. 4","2. 9","3. 10","4. 3",10)
    q_5=Question("5+1=","1. 1","2. 5","3. 8","4. 6",4)
    q_6=Question("3+5=","1. 8","2. 3","3. 9","4. 7",1)
    q_7=Question("2+5=","1. 3","2. 5","3. 4","4. 7",4)
    q_8=Question("1+9=","1. 5","2. 10","3. 9","4. 7",2)
    q_9=Question("5+2=","1. 9","2. 4","3. 7","4. 8",3)
    q_10=Question("4+6=","1. 10","2. 4","3. 2","4. 3",1)
    
    #N=int(input("Please enter the first turn (1-player_1, 2-player_2): "))
    #print(q_1.get_trivia_question())
    #print(q_2.get_trivia_question())
    #print(q_3.get_trivia_question())
    #print(q_4.get_trivia_question())
    #print(q_5.get_trivia_question())
    #print(q_6.get_trivia_question())
    #print(q_7.get_trivia_question())
    #print(q_8.get_trivia_question())
    #print(q_9.get_trivia_question())
    #print(q_10.get_trivia_question())
    
    player1_total=0
    player2_total=0   
    for i in range(10) :
        r=random.randint(0,10)
        if r==1:
           q=q_1
        elif r==2:
           q=q_2
        elif r==3:
           q=q_3
        elif r==4:
           q=q_4
        elif r==5:
            q=q_5
        elif r==6:
            q=q_6
        elif r==7:
            q=q_7
        elif r==8:
            q=q_8
        elif r==9:
            q=q_9
        elif r==10:
            q=q_10
        
        print(q.get_trivia_question())
        print(q.get_possible_answer_1())
        print(q.get_possible_answer_2())
        print(q.get_possible_answer_3())
        print(q.get_possible_answer_4())
        answer_1=int(input('Enter the answer player_1: '))
        answer_2=int(input('Enter the answer player_2: '))
        if answer_1==q.get_numb_corr():
            player1_total+=1
        if answer_2==q.get_numb_corr():
            player2_total+=1
            
        print(player1_total) 
        print(player2_total) 
        if  player1_total>player2_total:
            print("player 1 won")
        elif player1_total<player2_total:
            print("player 2 won")
        else:
            print("Both won")
main()