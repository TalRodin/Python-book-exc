import book

def main():
    info=input().split()
    b=book.Book(info[0],info[1],info[2])
    i=str(b)   
    print(i)

    
main() 
