print('--'*10)
def main():    
    try:
        outfile=open('golf.txt','w')
        for i in range(5): 
            name, score=input().split(' ') 
            outfile.write(name+' '+score+'\n')
            #print(name, score)
        outfile.close()
    except ValueError:
        print('Error')
    read_file(outfile)   
def read_file(outfile):
    try:
        infile=open('golf.txt', 'r')
        infile_content=infile.read()
        print(infile_content)
        infile.close()
    except ValueError:
        print('Error') 
main()
