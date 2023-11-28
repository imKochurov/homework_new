# TASK 1

# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!

from functools import wraps

def info_decorator(func):
    @wraps(func)
    def wrapper(*args):
        name = func.__name__                # зберігаємо ім'я функції
        print(f"\nІм'я функції: {name}", f"Аргументи функції: {args}", sep="\n")  # виводимо ім'я функції та передані аргументи
        result = func(*args)
        return result                       # повертаємо результат функції
    return wrapper

@info_decorator
def list_maker_function(*args):             # Тестова функція, яка генерує список із переданих аргументів.
    res = [i for i in args]
    print("\nРезультат виконання функції:")
    return res                              # за допомогою декоратора будемо виводити ім'я цієї функції та її аргументи

print(list_maker_function("abc", 74, {3, 2, 1}, True, ["a", "z"]), "\n") # Передаємо функції довільні аргументи для перевірки роботи декоратору


# TASK 2

# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

stop_words = ["russia", "moscow", "putin"] # перелік заборонених слів

def stop_russia(stop_list:list):
    def decorator(func):
        @wraps(func)
        def wrapper(arg:str):
            a = 0                           # змінна для підрахунку кількості замін в рядку
            for i in stop_list:             # перебираємо заборонені і слова, і якщо вони є у функції, робимо заміну в рядку 40
                if i in arg:
                    a += arg.count(i)       # додаємо кількість замін кожного стоп-слова
                arg = arg.replace(i, "*")
            print(f"\nУ введеному рядку виконано {a} замін.\n\nРядок з виключеними стоп-словами:")
            return arg                      # даний декоратор не враховує регістру, і робить заміну рядка лише у прямій відповідності до елементів списку stop_words
        return wrapper
    return decorator

@stop_russia(stop_list=stop_words)
def input_funk(a:str):
    return a

print(input_funk("moscow is the capital of russia, putin is the president of russia."), "\n")


# TASK 3

# Write a decorator "arg_rules" that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain

def verify_funk(type_:type, max_lenth:int, contains:list): #декоратор з трьома змінними для перевірки
    def decorator(func):
        @wraps(func)
        def wrapper(arg:str):
            if type(arg) != type_:
                print("\nНевірний тип даних!")
                return False
            elif len(arg) > max_lenth:
                print(f"\nДовжина введеного рядка перевищує {max_lenth} символів!")
                return False
            for i in contains:
                if str(i) not in arg:
                    print(f"\nУ введеному рядку відсутнє значення: '{i}'")
                    return False
            result = func(arg)
            return result
        return wrapper
    return decorator


@verify_funk(type_=str, max_lenth=15, contains=["05", "@"]) # передаємо в декоратор значення змінних для перевірки
def input_funk(arg):
    return f"\nUsername '{arg}' задовольняє умовам і може бути використаний."

print(input_funk("user@05")) # викликаємо функцію, передаємо їх наш юзернейм і перевіряємо умови, зазначені вище в декораторі