import json
import os
import time

# Функція приймає список з паролями.
# Повертає новий список списків, в значеннях якого відображені лише ті символи, які мають повторення для кожного паролю

def find_doubles(input_list:list):
    a = list()
    for i in input_list:
        b = set()
        for j in i:
            if i.count(j) > 1:
                b.add(j)
        a.append(list(b)) 
    proc_id = os.getpid()
    return [proc_id, a]



if __name__ == '__main__':
    with open('lesson27/random_passwords.json', 'r') as file:
        passwords_list = json.load(file)
    
    print('CUSTOM FUNCTION:')
    start = time.time()
    print(find_doubles(input_list=passwords_list))
    end = time.time()
    print(f'ЧАС ВИКОНАННЯ ФУНКЦІЇ: {round(end - start, 3)} сек')
