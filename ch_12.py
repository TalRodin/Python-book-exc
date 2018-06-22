# chapter 12

#1

def main():
    n=int(input())
    print_numbers(n)
def print_numbers(n):
    
    if n>0:
        print(n)
        print_numbers(n-1)
        
main()

#2

def main():
    x=int(input())
    y=int(input())
    
    s=sum_(x,y)
    print(s)
def sum_(x,y):
    
    if x==0:
        return 0
    elif x==1:
        return y
    else:
        return y+sum_(x-1, y)

    
main()

#3

#4

#5

#6

#7

#8

