# TASK 1

# Напишіть програму на мові Python для визначення кількості локальних змінних, оголошених у функції

def no_parameters_function(): # Порожня функція
    pass

def sum_lists(a, b): # Функція з двома аргументами для додавання елементів двох однакових за довжиною списків
    c = map(sum, zip(a, b))
    return(list(c))

def make_list(*args): # Функція для створення списку із будь-якої кількості аргументів
    output = [i for i in args]
    return(output)

func_to_test = sum_lists
code_object = func_to_test.__code__
num_locals = code_object.co_nlocals

print(f"Функція {func_to_test.__name__} містить в собі {num_locals} локальних змінних\n")

# Для вирішення задачі використовую атрибут 'co_nlocals'. На прикладі тьрох функцій.
# Як я зрозумів, 'co_nlocals' повертає сумарне значення змінних і параметрів функції.
# Дле першої функції буде 0, для другої 3 (параметри a, b і змінна с), для третьої функції 2 (args, output)

# TASK 2

# Напишіть програму на Python для доступу до функції всередині функції

import json
from random import randint

def random_list_maker_writer(count_list):
    for i in range(count_list):
        rd_list = [chr(i + randint(65, 85)) for i in range(0, 6)]

        def input_writer_fucnion():
            with open(f"users_{i+1}.json", "w") as file:
                json.dump(rd_list, file)

        input_writer_fucnion()

    return(print(f"Було записано {count_list} файлів з випадковим набором букв.\n"))

# random_list_maker_writer(3)

# Зовнішня функція приймає параметр, скільки json-файлів з рандомними списками треба записати
# Внутрішня функція запису викликається всередині зовнішньої функції

# TASK 3

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def choose_func(nums_list):
    has_negative = any(num < 0 for num in nums_list)
    if has_negative == True: #якщо є від'ємні числа
        return(remove_negatives(nums_list))
    else:
        return(square_nums(nums_list))

print(choose_func(nums2))