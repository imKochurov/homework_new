# TASK 1

class Animal:
    def __init__(self, animal_name):
        self.animal_name = animal_name

    def talk(self):
        return f"{self.animal_name} can't talk"
    
class Cat(Animal):
    def talk(self):
        return f"{self.animal_name} say 'Meow!'"
    
class Dog(Animal):
    def talk(self):
        return f"{self.animal_name} say 'Woof!'"
    
c = Cat("Kokos")
d = Dog("Marty")
print(c.talk(), d.talk(), sep = "\n")


# TASK 2 

class Author:
    def __init__(self, author_name, country, birthday):
        self.author_name = author_name
        self.country = country
        self.birthday = birthday

    def __str__(self):
        return f"class Author: information about {self.author_name}."

    def author_info(self):
        return {self.author_name: {"country": self.country, "birthday": self.birthday}}
    
author1 = Author("Stephen King", "USA", "21.09.1947")
# print("\n", author1.author_info())

class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def __str__(self):
        return f"class Book: information about book '{self.title}'."
        
    def book_info(self):
        return {"book name": self.title, "book year": self.year, "author": self.author.author_name}
    
book1 = Book("The Shining", 1977, author=author1)
book2 = Book("Pet Sematary", 1983, author=author1)
book3 = Book("The Dark Tower", 1970, author=author1)

# print("\n", book1.book_info(), book2.book_info(), book3.book_info(), sep="\n")

class Library:
    library_dict = {}
    def __init__(self, library_name):
        self.library_name = library_name

    def __str__(self):
        return f"class Library: '{self.library_name}', Ukraine."

    def new_book(self, book):
        return self.library_dict.update({book.title: {"author": book.author.author_name, "year": book.year, "country": book.author.country}})
    
    def group_by_author(self, author):
        a_ = []
        for i in self.library_dict:
            if self.library_dict.get(i).get("author") == author:
                a_.append(i)
        return f"All books written by {author} in our library: {a_}"
    
    def group_by_year (self, year):
        a_ = []
        for i in self.library_dict:
            if self.library_dict.get(i).get("year") == year:
                a_.append(i)
        return f"All books written in {year} in our library: {a_}"

Library("Grand Library").new_book(book1)
Library("Grand Library").new_book(book2)
Library("Grand Library").new_book(book3)

print("\n", "Database of our library: ", Library("Grand Library").library_dict)
print("\n", Library("Grand Library").group_by_author("Stephen King"))
print("\n", Library("Grand Library").group_by_year(1977))


# TASK 3

class Fraction:
    def __init__(self, numerator1, denominator1):
        self.numerator1 = numerator1
        self.denominator1 = denominator1

    def decorator(func): # декоратор скорочення дробу за алгоритмом Евкліда
        def wrap(*args):
            try:
                result = func(*args)
                a = result[0]
                b = result[1]
                while b:
                    a, b = b, a % b
                num = result[0]//a
                denom = result[1]//a
                if num >= denom:
                    return f"Результат методу {func.__name__}: {num//denom}"
                else:
                    return f"Результат методу {func.__name__}: {num}/{denom}"
            except Exception as e:
                return f"В методі {func.__name__} виникла помилка: {type(e).__name__}: {str(e)}"
        return wrap

    @decorator
    def __add__(self, numerator2, denominator2):
        num = self.numerator1*denominator2 + numerator2*self.denominator1
        denom = self.denominator1*denominator2
        return num, denom
    
    @decorator
    def __mul__(self, numerator2, denominator2):
        num = self.numerator1*numerator2
        denom = self.denominator1*denominator2
        return num, denom
    
    @decorator
    def __sub__(self, numerator2, denominator2):
        num = self.numerator1*denominator2 - numerator2*self.denominator1
        denom = self.denominator1*denominator2
        return num, denom
    
    @decorator
    def __truediv__(self, numerator2, denominator2):
        if denominator2 == 0:
            raise ZeroDivisionError("ділення на нуль")
        else:
            num = self.numerator1*denominator2
            denom = self.denominator1*numerator2
            return num, denom

a = Fraction(5, 8)

print("\n", a.__add__(1, 4), a.__sub__(1, 5), a.__mul__(1, 3), a.__truediv__(3, 16), sep="\n")
