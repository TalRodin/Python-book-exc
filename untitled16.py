import random
def main():
   country_capital={}
   country_capital['Russia']='Moscow'
   country_capital['USA']='WashingtonDC'
   country_capital['France']='Paris'
   country_capital['UK']='London'
   #print(country_capital)

   
   
   
   count_correct=0
   count_incorrect=0
   for country in country_capital:
       country=random.choice(list(country_capital))
       print(country)
       capital=input("Please enter the capital: ")
       for key in country_capital:
       
           if capital==country_capital[key]:
           #print("Correct")
               count_correct+=1
           else:
           #print("Incorrect")
               count_incorrect+=1
   print(count_correct)
   print(count_incorrect)
main()
