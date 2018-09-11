#1 Suppose my_car is the name of a variable that references an object
#  and go is the name of a method. Write a statement that uses the my_car
#  variable to call the go method. (You don't have to pass any arguments to 
#  the go method). Confused here if someone could help, would be thankful.
class Car:
    def __init__(self, my_car):
        self.__my_car=my_car
    def set_my_car(self, my_car):
        self.__my_car=my_car
    def get_my_car(self):
        return self.__my_car


#2 

class Book:
    def __init__(self, title, author, publisher):
        self.__title=title
        self.__author=author
        self.__publisher=publisher
    
    def set_title(self, title):
        self.__title=title
    def set_author(self, author):
        self.__author=author
    def set_publisher(self, publisher):
        self.__publisher=publisher
    
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_publisher(self):
        return self.__publisher

    def __str__(self):
        return self.__title

import book

def main():
    info=input().split()
    b=book.Book(info[0],info[1],info[2])
    
main()        