    # TASK 1

def oops(): # функція з помилкою IndexError
    raise IndexError

def oops2(): # except помилки IndexError
    try:
        oops()
    except IndexError:
        print("Try-Except Homework")

def oops3(): # except помилки KeyError
    try:
        oops()
    except KeyError:
        print("Try-Except Homework")

# oops()
# oops2()
# oops3()

    # TASK 2

def input_function():
    print("Розрахуємо вираз 'a**2/b'.")
    a = int(input("Введіть ціле число 'a': "))
    b = int(input("Введіть ціле число 'b': "))
    c = a**2/b
    print(f"a**2/b = {c}")

try:
    input_function()
except (ZeroDivisionError, ValueError):
    print("БІДА... Ви ввели шось не те...")


