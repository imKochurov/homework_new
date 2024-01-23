# КОМЕНТАР. Суть мого коду - у файлі HW_random_passwords_generator.py я генерую список із "паролів" - наборів із цифр і букв різних регістрів.
# Даний список збережено у файл random_passwords.json
# Далі, я зробив звичайну функцію (файл HW_doubles_finder.py), яка перебирає ці паролі у списку і в кожному знаходить символи, які повторюються -
# ця функція повертає список списків формату: [[], ['4', 'f', 'T'], ['6'], ['5', '9'], []], де послідовно для кожного паролю видно повторювані символи

# І, нарешті, в цьому файлі я використовую мультипроцесинг, де розбиваю вхідний список на 4 частини і створюю 4 процеси, які мають обробити
# частини списку і потім об'єднати його в один і повернути, використовуючи вище описану функцію.

# За допомогою модуля os відстежую ID кожного процесу, і дійсно видно, що логіка роботи правильна, вхідний список розділяється на частини, обробляється
# окремими процесами і в кінці об'єднується

# АЛЕ... з невеликим списком все працює, а коли генерую довгий список, біля 1500000 значень - звичайна функція спрацьовує за 14-15 секунд,
# а мій мультипроцесинг зависає дуже надовго...

# я наче розібрався як це все написати в python, але просто не дуже розумію логіку "під капотом", мабуть моя задача не дуже вдала...
# лишив короткий список, щоб швидше побачити, що розділення процесів таки відбувається
# але, виграші в часі виконання коду я так і не зумів добитися

# можливо, значна додаткова частина часу витрачається на розбиття списку на частини плюс робота класу Queue (я його використав, щоб результати
# чотирьох моїх процесів на виході об'єднати в один список)


import json
from multiprocessing import Process, Queue
import os
import time


def find_doubles(input_list:list, result_q):
    a = list()
    for i in input_list:
        b = set()
        for j in i:
            if i.count(j) > 1:
                b.add(j)
        a.append(list(b))
    proc_id = os.getpid() # визначаємо ID процесу, щоб далі переконатися, що мультипроцессинг працює
    result_q.put([proc_id, a]) # метод put класу Queue


def mult_processes(in_list, processes = 4):

    # Розділення словника на вказану кількість частин
    total_values = len(in_list)
    part_lenght = total_values // processes # Ділимо список на 4 рівні частини
    remaining_values = total_values % processes # Кількість значень в остачі, яка завжди буде менше 4, як зазначено в змінній processes

    result_q = Queue() # клас для обміну даними, щоб після завершення процесів можна було розбиті оброблені списки знову "зліпити" в один цілий
    mult_processes = []

    start_index = 0
    for i in range(processes):
        end_index = start_index + part_lenght + (1 if i < remaining_values else 0) # формуємо кінцевий індекс для зрізу словника, додаємо додатково по 1 значенню в кожну частину, якщо була остача
        proc = Process(target=find_doubles, args=(in_list[start_index : end_index], result_q)) # зрізом формуємо частину словника, яку передаємо в процес
        mult_processes.append(proc)
        proc.start()
        start_index = end_index
    
    for proc_ in mult_processes:
        proc_.join()

    results = []
    while not result_q.empty(): # метод empty класу Queue
        results.append(result_q.get()) # метод get класу Queue
    
    return results




if __name__ == '__main__':
    with open('lesson27/random_passwords.json', 'r') as file:
        passwords_list = json.load(file)

    print('MULTIPROCESSING FUNCTION:')
    start = time.time()
    print(mult_processes(in_list=passwords_list))
    end = time.time()
    print(f'ЧАС ВИКОНАННЯ ФУНКЦІЇ: {round(end - start, 3)} сек')