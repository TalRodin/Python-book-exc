#1

def main():
    list_=[]
    n=int(input())
    for i in range(n):
        list_.append(input())
    print(list_)
    name(list_)

#2

print('------')
def name(list_):    
    for i in list_:
        print(i)

main()

#3

print('------')
def main():
    number1=[1,2,3,4,5]
    number2=[]
    for i in number1:
        number2.append(i)
    print(number2)
main()

#4

#draw flowchart

#5

print('------')
def main():
    list_=[1,2,3,4,5,6]
    total(list_)
def total(list_):
    total=0
    for i in list_:
        total+=i
    print(total)

main()

#6

print('------')
def main():
    list_=['Ruby', 'Nadia', 'Yudi', 'Joshua']
    name_(list_)
def name_(list_):
    name='Ruby'
    if name in list_:
        print(name)
    else:
        print('No Ruby')
main()


#7

print('------')
list1=[40, 50, 60]
list2=[10, 20, 30]
list3=list1+list2
print(list3)

#8

print('------')
def main():
    list_=[]
    for i in range(5):
        list_+=[[int(input()) for j in range(3)]]
    for element in list_:
        print('{:5}{:5}{:5}'.format(element[0],element[1],element[2]))   
main()
