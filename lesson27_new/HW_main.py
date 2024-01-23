# КОМЕНТАР. Суть мого коду - у файлі HW_random_passwords_generator.py я генерую список із "паролів" - наборів із цифр і букв різних регістрів.
# Даний список збережено у файл random_passwords.json
# Далі, я зробив звичайну функцію (файл HW_doubles_finder.py), яка перебирає ці паролі у списку і в кожному знаходить символи, які повторюються -
# ця функція повертає список списків формату: [[], ['4', 'f', 'T'], ['6'], ['5', '9'], []], де послідовно для кожного паролю видно повторювані символи

# І, нарешті, в цьому файлі я використовую мультипроцесинг, де автоматично розбиваю вхідний список і створюю процеси, які мають обробити
# частини списку і потім об'єднати його в один і повернути.





from lesson21.lesson_21_homework import Time_ # кастомний контекстний менеджер для вимірювання часу роботи коду із домашки №21
import json
import multiprocessing


def find_doubles(input:str):
    b = set()
    for j in input:
        if input.count(j) > 1:
            b.add(j)
    return list(b)


def mult_processes(in_list):
    with multiprocessing.Pool() as pool:
        results = pool.map(find_doubles, in_list)
    squared_numbers = results
    return squared_numbers
    


if __name__ == '__main__':
    with open('lesson27_new/random_passwords.json', 'r') as file:
        passwords_list = json.load(file)

    print('MULTIPROCESSING FUNCTION:')
    with Time_():
        mult_processes(in_list=passwords_list)

# РЕЗУЛЬТАТИ:
        
# CUSTOM FUNCTION:
# ЧАС ВИКОНАННЯ КОДУ: 11.524 секунд
        
# MULTIPROCESSING FUNCTION:
# ЧАС ВИКОНАННЯ КОДУ: 7.425 секунд