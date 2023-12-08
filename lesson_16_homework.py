from datetime import datetime # для виконання 4-го завдання

# TASK 1

class Person:
    def __init__(self, full_name, age, department):
        self.full_name = full_name
        self.age = age
        self.department = department

    def dep(self):
        return f"{self.full_name} in {self.department} department (method from claas Person)"

class Student(Person):
    def __init__(self, full_name, age, department, group_num, average_score):
        super().__init__(full_name, age, department)
        self.group_num = group_num
        self.average_score = average_score

    def student_info(self):
        return f"Student {self.full_name} studies at the department of {self.department} in {self.group_num} group.\nStudent {self.full_name} has {self.average_score} points."
    
class Teacher(Person):
    def __init__(self, full_name, age, department, subject, salary):
        super().__init__(full_name, age, department)
        self.subject = subject
        self.salary = salary
    
    def teacher_info(self):
        return f"Teacher {self.full_name} works at {self.department} and has salary {self.salary}$. Subject: {self.subject}."
    
stud1 = Student("John Smith", 22, "Mathematics", "A_17B", 10.47)
teach1 = Teacher("Anna Jablonska", 43, "Physics", "Theoretical Mechanics", 750)

print(stud1.dep(), stud1.student_info(), sep="\n")
print("\n", teach1.dep(), teach1.teacher_info(), sep="\n")


# TASK 2

class Mathematician:
    def square_nums(self, input_list:list):
        return [i**2 for i in input_list]

    def remove_positives(self, input_list:list):
        def condition(num):
            return num < 0
        return list(filter(condition, input_list))

    def filter_leaps(self, input_list:list):
        def condition(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        return list(filter(condition, input_list))

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


# TASK 3

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

p1 = Product("smartphone", "Samsung_A52", 15600)
p2 = Product("sneakers", "Adidas_HQ4376", 4650)
p3 = Product("sweets", "TOBLERONE_White_100g", 65)
p4 = Product("smartphone", "Xiaomi_Redmi_12_pro", 9800)

class ProductStore:
    product_list = {}
    profit = 0

    def __init__(self):
        self.markup = 0.3

    def add(self, product, count:int):
        if product.name not in self.product_list:
            self.product_list.update({product.name: {"type": product.type, "price": product.price*(1+self.markup), "count": count, "profit": 0}})
        else:
            self.product_list[product.name]["count"] += count
        return self.product_list

    def set_discount(self, product, discount):
        if product.name in self.product_list:
            self.product_list[product.name]["price"] *= 1 - discount/100
            return self.product_list
        else:
            return f"{product.name} not in Product List. Please, firstly add product to set discount."
        
    def sell_product(self, product, count):
        if count <= self.product_list[product.name]["count"] and count > 0:
            self.product_list[product.name]["count"] -= count
            self.profit += (self.product_list[product.name]["price"] - self.product_list[product.name]["price"]/(1+self.markup))*count
            self.product_list[product.name]["profit"] += (self.product_list[product.name]["price"] - self.product_list[product.name]["price"]/(1+self.markup))*count
            return self.profit
        else:
            return "ERROR: Unable to make a sale!"

    def get_income(self, product):
        return self.product_list[product.name]["profit"]
    
    def get_all_products(self):
        return [i for i in self.product_list]
    
    def get_product_info(self, product):
        return product.name, self.product_list[product.name]["count"]


ProductStore().add(p1, 5)
ProductStore().add(p2, 3)
ProductStore().add(p3, 7)
ProductStore().add(p4, 4)
print("\n", ProductStore().product_list) # рядок 112-115 - додали товари в словник товарів магазину, виводимо словник на перегляд
print("\n", ProductStore().set_discount(p2, 10)) # Застосовуємо знижку 10% до другого товару, переписуємо ціну в словнику
ProductStore().sell_product(p1, 3) # Продаємо 3 смартфони із 5 наявних
print("\n", ProductStore().get_product_info(p1)) # Переглядаємо інформацію по товару - кортеж з назвою і кількістю в залишку (2 смартфони лишилося)
print("\n", ProductStore().get_income(p1)) # Прибуток від 3 проданих смартфонів (ціна магазину мінус вхідна ціна без націнки)
print("\n", ProductStore().get_all_products()) # Список усіх наявних товарів в магазині
print("\n", ProductStore().product_list) # Просто переглядаємо словник товарів магазину після всіх проведених операцій


# TASK 4

class CustomException(Exception):
    def __init__(self, messege):
        super().__init__(messege)
        with open("logs.txt", "a") as file:
            file.write(f"{datetime.now()} Error: {messege}\n")

try:
    a = 10/0
    
except Exception as e:
    CustomException(f"{type(e).__name__}, {e.args[0]}")
