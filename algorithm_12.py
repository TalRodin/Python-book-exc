#1
#the program display 10
def main():
    num=0
    show_me(num)
def show_me(arg):
    if arg<10:
        #print(arg)
        show_me(arg+1)
        
    else:
        print(arg)
main()

#2
# there is a mistyping in line (if arg 10)
# the program display 0...10
def main():
    num=0
    show_me(num)
def show_me(arg):
    print(arg)
    if arg < 10:
        show_me(arg+1)
        
main()

#3

def main():
    n=0
    traffic_sign(n)
def traffic_sign(n):    
    print('No Parking')
    if n<1:
        traffic_sign(n+1)

main()






