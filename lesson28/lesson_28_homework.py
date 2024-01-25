from threading import Thread
import json
from lesson21.lesson_21_homework import Time_
import time

# Моя функція приймає список із рядків (str), в кожному рядку шукає символи, що повторюються.
# Функція повертає список списків із повторюваних символів для кожного рядка

def find_doubles(input_list:list):
    print('START')
    a = list()
    for i in input_list:
        b = set()
        for j in i:
            if i.count(j) > 1:
                b.add(j)
        a.append(list(b))
    print('END') 
    return a

# Тут хочу розділити мій список навпіл зрізами, і двома потоками обробити по пів-списка

def threaded_processing(input_array):
    res = []
    div_ = len(input_array)//2
    t1 = Thread(target=lambda x:res.extend(find_doubles(x)), args=(input_array[:div_],))
    t2 = Thread(target=lambda x:res.extend(find_doubles(x)), args=(input_array[div_:],))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return res

# Перевіряємо

with open('lesson28/random_passwords.json', 'r') as file:
    passwords_list = json.load(file)

print('CUSTOM FUNCTION:')
with Time_():
    find_doubles(input_list=passwords_list)

print('THREADING FUNCTION:')
with Time_():
    threaded_processing(input_array=passwords_list)

    # РЕЗУЛЬТАТ:

    # CUSTOM FUNCTION:
    # START
    # END
    # ЧАС ВИКОНАННЯ КОДУ: 12.022 секунд

    # THREADING FUNCTION:
    # START
    # START
    # END
    # END
    # ЧАС ВИКОНАННЯ КОДУ: 11.533 секунд
        
    # КОМЕНТАР: Суть задачі продублював із попереднього завдання з мультипроцесингом.
        # Коли ОДНА функція має обробити ОДИН список по частинам.
        # В мультипроцесингу це дозволило скоротити час виконання коду майже вдвічі
        # В цій ситуації, економії по часу не спостерігається, думаю через те, що тут немає повноцінної "паралельності" задач,
        # і процеси все одно перемикаються послідовно - мені здається, що на етапі "витягування" даних з ОДНОГО масиву.

    # Спробуємо розбити список не в тілі функції, а створити два окремих файли по пів-списку, тоді:

# div_ = len(passwords_list)//2

# with open('lesson28/part1.json', 'w') as file:
#     json.dump(passwords_list[:div_], file, indent=2)

# with open('lesson28/part2.json', 'w') as file:
#     json.dump(passwords_list[div_:], file, indent=2)
    
with open('lesson28/part1.json', 'r') as file:
    part1 = json.load(file)

with open('lesson28/part2.json', 'r') as file:
    part2 = json.load(file)


def threaded_processing_22(input_array1, input_array2):
    res = []
    t1 = Thread(target=lambda x:res.extend(find_doubles(x)), args=(input_array1,))
    t2 = Thread(target=lambda x:res.extend(find_doubles(x)), args=(input_array2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return res

print('THREADING FUNCTION 2:')
with Time_():
    threaded_processing_22(input_array1=part1, input_array2=part2)

    # РЕЗУЛЬТАТ:

    # CUSTOM FUNCTION:
    # START
    # END
    # ЧАС ВИКОНАННЯ КОДУ: 12.154 секунд

    # THREADING FUNCTION:
    # START
    # START
    # END
    # END
    # ЧАС ВИКОНАННЯ КОДУ: 11.692 секунд

    # THREADING FUNCTION 2:
    # START
    # START
    # END
    # END
    # ЧАС ВИКОНАННЯ КОДУ: 12.523 секунд

    # КОМЕНТАР: не помогло )))))))
    # Остання теорія: зробимо два дублікати початкової функції, визначимо їх як різні, і обробимо розбиті файли

def find_doubles_11(input_list:list):
    print('START')
    a = list()
    for i in input_list:
        b = set()
        for j in i:
            if i.count(j) > 1:
                b.add(j)
        a.append(list(b))
    print('END') 
    return a

def find_doubles_22(input_list:list):
    print('START')
    a = list()
    for i in input_list:
        b = set()
        for j in i:
            if i.count(j) > 1:
                b.add(j)
        a.append(list(b))
    print('END') 
    return a

def threaded_processing_33(input_array1, input_array2):
    res = []
    t1 = Thread(target=lambda x:res.extend(find_doubles_11(x)), args=(input_array1,))
    t2 = Thread(target=lambda x:res.extend(find_doubles_22(x)), args=(input_array2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return res

print('THREADING FUNCTION 3:')
with Time_():
    threaded_processing_33(input_array1=part1, input_array2=part2)

    # РЕЗУЛЬТАТ:

    # THREADING FUNCTION 3:
    # START
    # START
    # END
    # END
    # ЧАС ВИКОНАННЯ КОДУ: 11.838 секунд

    # КОМЕНТАР: Очевидно, ща наша конкретна задача роботи з масивами в кількох потоках не реалізує повноцінний "паралельний" алгоритм, як мультипроцесинг
    # Певно, це обмеження, пов'язані з Global Interpreter Lock

    # В рамках нашого завдання видно, що для подібних задач багатопоточність не є ефективною
    # Напевно, потоки краще використати для одночасних API-запитів, запису файлів, запитів до баз даних тощо



def task1():
    print('Task1 STARTED')
    time.sleep(2)
    print('Task1 COMPLETED')

def task2():
    print('Task2 STARTED')
    time.sleep(3)
    print('Task2 COMPLETED')

def task3():
    print('Task3 STARTED')
    time.sleep(1)
    print('Task3 COMPLETED')


with Time_():
    thread1 = Thread(target=task1)
    thread2 = Thread(target=task2)
    thread3 = Thread(target=task3)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
