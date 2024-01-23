from lesson21.lesson_21_homework import Time_
import json

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
    return a



if __name__ == '__main__':
    with open('lesson27_new/random_passwords.json', 'r') as file:
        passwords_list = json.load(file)
    
    print('CUSTOM FUNCTION:')
    with Time_():
        find_doubles(input_list=passwords_list)
