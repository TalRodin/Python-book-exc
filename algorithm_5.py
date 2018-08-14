#1
def times_ten(x):
     return(int(x)*10)

if __name__=='__main__':
    
     x=input()
     y=times_ten(x)
     print(y)
     
#2

def show_value(quantity):
    print(quantity)


if __name__=='__main__':
    show_value(int(input()))
    
#5

def my_function(a,b,c):
    d=(a+c)/b
    print(d)
if __name__=='__main__':
    my_function(2,4,6)
    
#6

import random
print(random.randint(1,100))

#7
def half(number):
    return(number/2)

if __name__=='__main__':
    n=float(input())
    print(half(n))
    
#8

def cube(num):
    return (num*num*num)

if __name__=='__main__':
    result=input()
    print(cube(int(result)))
    
#9

def times_ten(x):
     return(x*10)

if __name__=='__main__':
    
     x=input()
     y=times_ten(x)
     print(y)
    
#10

def get_first_name():
     name=input("Name: ")
     return name

if __name__=='__main__':
     y=get_first_name()
     print(y)

