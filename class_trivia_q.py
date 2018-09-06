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