#1

d={}
d['a']=1
d['b']=2
d['c']=3
print(d)

#2

d={}

#3

dct={}
dct['James']=90
if 'James' in dct:
    print(dct['James'])
else:
    print('Not in dictionary')
    
#4

dct_={}
dct_['jim']=90
dct_['elli']=98
if 'jim' in dct_:
    dct_.pop('jim')
print(dct_)

#5

set([10,20,30,40])

#6

set1=set([1,2,3])
set2=set([10,20,30])
set3=set1.union(set2)
print(set3)

#7

set1=set([1,2,3,10])
set2=set([10,20,30])
set3=set1&set2
print(set3)

#8

set1=set([1,2,3,10])
set2=set([10,20,30])
set3=set1-set2
print(set3)

#9

set1=set([1,2,3,10])
set2=set([10,20,30])
set3=set2-set1
print(set3)

#10

set1=set([1,2,3,10])
set2=set([10,20,30])
set3=set2^set1
print(set3)

#11

import pickle
d={}
d['a']=1
d['b']=2
d['c']=3
output_file=open('mydata.dat','wb')
pickle.dump(d,output_file)
output_file.close()

#12

input_file=open('mydata.dat','rb')
pb=pickle.load(input_file)
print(pb)






















