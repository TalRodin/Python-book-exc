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

def main():
    n=int(input())
    aster(n)
def aster(n):
    if n>0:
        aster(n-1)
        print('*'*n)
        
main()

#4


def main():
    n=[5,7,6,10,2]
    f=find_large(n)
    print(f)
def find_large(n):
    
    if len(n)==1:
        return(n[0])
    else:                
        return(max(n[1:]) if max(n[1:])>n[0] else n[0])
main()

#5
def main():
    list_=[4,5,6,3]
    f=find_sum(list_)
    print(f)
def find_sum(list_):
    if len(list_)==1:
        return(list_[0])
    else:
        return(list_[0]+find_sum(list_[1:]))
    

main()

#6

def main():
    n=int(input())
    s=sum(n)
    print(s)
def sum(n):
    if n== 0:
        return 0
    else:
        return n + sum(n-1)
        
main()

#7

def main():
    x=int(input())
    y=int(input())
    
    p=power(x,y) 
    print(p)
def power(x,y):
    if y==0:
        return 1
    if y>0: 
        
        return(x*power(x,y-1))
main()
    

#8

def main():
    x=int(input())
    y=int(input())
    ackermann(x,y)
def ackermann(x,y):
    if x==0:
        return (y+1)
    if y==0:
        return(ackermann(x-1,1))
    else:
        return(ackermann(x-1, ackermann(x,y-1)))
    
main()