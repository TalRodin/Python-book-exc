#1
y=''
z=''
t=list(map(int,input().split()))
x=sum(t)
if x>100:
    y=20
    z=40
print(y,' ',z)

#2
b=''
c=''
t=list(map(int, input().split()))
x=sum(t)
if x<10:
    b=0
    c=1
print(b, ' ',c)

#3
b=''
t=list(map(int, input().split()))
a=sum(t)
if a<10:
   b=0
else:
   b=99
print(b)

#4
if score>= A_score:
    print('Your grade is A. ')
elif score>=B_score:
    print('Your grade is B. ')
elif score>=C_score:
    print('Your grade is C. ')
elif score>=D_score:
    print('Your grade is D. ')
else:
    print('Your grade is F. ')
    
#5
if amount1>10 and amount2<100:
    if amount1>amount2:
        print(amount1)
    else:
        print(amount2)
        
#6
if variable>24 and variable<56:
    print("Speed is normal")
else:
    print("Speed is abnormal")
        
#7
if variable>9 and variable<51:
    print("Valid points")
else:
    print("Invalid points")





























