# TASK 1

# f = open('myfile.txt', 'w')
# f.write('Hello file world!\n')
# f.close()

# f1 = open('myfile.txt', 'r')
# print(f1.read())
# f1.close()


# TASK 2

import json

phonebook = [{'first_name': 'ILLIA', 'last_name': 'KOCHUROV', 'city': 'KREMENCHUK', 'phone': '+3801234569'},
             {'first_name': 'DMYTRO', 'last_name': 'VINNICHENKO', 'city': 'ZHYTOMYR', 'phone': '+380987654321'},
             {'first_name': 'KATERYNA', 'last_name': 'GLOBA', 'city': 'KYIV', 'phone': '+380504567812'}
             ]

with open('Phonebook_homework.json', 'w') as book: #Одноразовий запис телефонного довідника в файл json, для тестування програми. В подальшому цю команду і попередній словник закоментуватиб щоб не перезаписувати файл.
    book.write(json.dumps(phonebook))


def open_phonebook(): # Функція завантаження телефонного довідника
    with open('Phonebook_homework.json', 'r') as book1:
        return(json.loads(book1.read()))

def write_phonebook(y): # Функція перезапису довідника
    with open('Phonebook_homework.json', 'w') as book2:
        book2.write(json.dumps(y))

def add_new(x): # Додаємо новий контакт в список
    print('\nВведіть наступні дані:\n')
    first_name = input("Введіть ім'я: ").upper()
    last_name = input('Введіть прізвище: ').upper()
    city = input('Введіть назву міста: ').upper()
    phone = input('Введіть номер телефону: ')
    new_contact = {'first_name': first_name, 'last_name': last_name, 'city': city, 'phone': phone}
    a = list()
    a.append(new_contact)
    return(x+a)

def find_first_name(): # Шукаємо контакт за ім'ям
    print("\nШукаємо контакт за ім'ям:\n")
    first_name = input("Введіть ім'я: ").upper()
    result = list()
    for i in open_phonebook():
        if i.get('first_name') == first_name:
            result.append(i)
        else:
            pass

    if len(result) >= 1:
        print(result)
    else:
        print(f"Контактів з ім'ям {first_name} не знайдено.")

def find_last_name(): # Шукаємо контакт за прізвищем
    print("\nШукаємо контакт за прізвищем:\n")
    last_name = input("Введіть прізвище: ").upper()
    result = list()
    for i in open_phonebook():
        if i.get('last_name') == last_name:
            result.append(i)
        else:
            pass

    if len(result) >= 1:
        print(result)
    else:
        print(f"Контактів з прізвищем {last_name} не знайдено.")

def find_name(): # Шукаємо контакт за прізвищем та ім'ям
    print("\nШукаємо контакт за ім'ям та прізвищем:\n")
    first_name = input("Введіть ім'я: ").upper()
    last_name = input("Введіть прізвище: ").upper()
    result = list()
    for i in open_phonebook():
        if i.get('first_name') == first_name and i.get('last_name') == last_name:
            result.append(i)
        else:
            pass

    if len(result) >= 1:
        print(result)
    else:
        print(f"Контактів з ім'ям {first_name} та прізвищем {last_name} не знайдено.")

# Алгоритм пошуку за номером телефону та назвою міста буде аналогічним до функцій пошуку за ім'ям або прізвищем.
# На свій страх і ризик не пишу ці блоки, задля економії нашого спільного часу )))))

def delete_contact(): # Видаляємо контакт по номеру телефону
    number = input('\nВведіть номер телефону:\n')
    result = list()
    s = open_phonebook()
    for i in s:
        if i.get('phone') == number:
            result.append(i)
        else:
            pass
    
    if len(result) >= 1:
        for k in result:
            s.remove(k)
    else:
        pass
    write_phonebook(s)

def update_phone(): # Оновити контакт, пошук за номером
    delete_contact()
    print('\nВведіть оновлені дані цього контакту:\n')
    write_phonebook(add_new(open_phonebook()))

# ЗАПУСКАЄМО ПРОГРАМУ ДОВІДНИКА
while True:
    print("""
Вітаємо в телефонному довіднику!
Для перегляду довідника введіть 'open'.
Для додавання нового контакту введіть 'add'.
Для пошуку за ім'ям введіть 'first name'.
Для пошуку за прізвищем введіть 'last name'.
Для пошуку за прізвищем і ім'ям введіть 'all name'.
Для видалення контакту введіть 'del'.
Для оновлення існуючого контакту введіть 'update'.
Для виходу із програми введіть 'q'.
        """)
    user_choise = input()

    if user_choise == 'open':
        print("Перегляньте наявний довідник:", open_phonebook(), sep = '\n')
    elif user_choise == 'add':
        print("Додаємо новий контакт.")
        write_phonebook(add_new(open_phonebook()))
        print("Оновлений довідник:", open_phonebook(), sep = '\n')
    elif user_choise == 'first name':
        print("Шукаємо наявний контакт за ім'ям.")
        find_first_name()
    elif user_choise == 'last name':
        print("Шукаємо наявний контакт за прізвищем.")
        find_last_name()
    elif user_choise == 'all name':
        print("Шукаємо наявний контакт за ім'ям та прізвищем.")
        find_name()
    elif user_choise == 'del':
        print("Видаляємо наявний контакт за номером.")
        delete_contact()
        print(open_phonebook())
    elif user_choise == 'update':
        print("Оновлюємо інформацію в наявному контакті.")
        update_phone()
        print(open_phonebook())
    elif user_choise == 'q':
        print("Робота з програмою завершена.")
        break
    else:
        print('Ви ввели невіринй параметр, спробуймо ще раз!\n')
