#1

outfile=open('my_name.txt','w')
n=input()
outfile.write(n)
outfile.close()

#2

infile=open('my_name.txt','r')
print(infile.read())
infile.close()

#3

outfile=open('number_list.txt','w')
[outfile.write(str(i)+'\n') for i in range(1,100+1)]
outfile.close()

#4

infile=open('number_list.txt','r')  
print(infile.read())
infile.close()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
#5
infile=open('number_list.txt','r')
t=0
for line in infile:
    amount=float(line)
    t+=amount
infile.close()
print(t)

#6

outfile=open('number_list.txt','a')
outfile.write('Elli')
outfile.close()
print(outfile)


