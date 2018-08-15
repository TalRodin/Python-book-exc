#1

string=input()
choice=string.lower()
if choice=='y':
    print('Correct')
else:
    print('Incorrect')
#2

mystring=input()
total=0

for i in mystring:
    if i.isspace():
        total+=1
print(total)

#3

mystring=input()
total_digits=0
for i in mystring:
    if i.isdigit():
        total_digits+=1
print(total_digits)

#4

mystring=input()
total_lower=0
for i in mystring:
    if i.islower():
        total_lower+=1
print(total_lower)

#5

mystring=input()
if mystring.endswith('.com'):
    print(True)
else:
    print(False)

#6

mystring=input()
print(mystring.replace('t','T'))

#7

mystring=input()
mystring[-1::-1]


#8

mystring=input()
print(mystring[:3])

#9

mystring=input()
print(mystring[-1::-1][:3])

#10

mystring='cookies>milk>fudge>cake>ice cream'
mystring.split('>')

    




















