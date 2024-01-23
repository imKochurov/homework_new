import json
import random

# Функція генерує список паролів із цифр і літер різних регістрів, за введеними значеннями довжини списку та довжини паролю

def random_dict(list_len:int, value_len:int):
    lower_case = [chr(i) for i in range(97, 123)] # lower case
    upper_case = [chr(i) for i in range(65, 91)] # upper case
    numbers_ = [chr(i) for i in range(48, 58)] # numbers
    a = [lower_case, upper_case, numbers_]
    b = []
    for i in range(list_len):
        c = ''
        for _ in range(value_len):
            c += random.choice(random.choice(a))
        b.append(c)
    return b



if __name__ == '__main__':
    res = random_dict(list_len=5, value_len=10)
    # print(res)

    with open('lesson27/random_passwords.json', 'w') as file:
        json.dump(res, file, indent=2)

