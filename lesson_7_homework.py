# TASK 1

dict_final = dict()

while True:
    a = input('Введіть слово. Для виходу з програми введіть "q":\n')
    if a == 'q':
        break
    elif dict_final.get(a) == None:
        dict_final.update({a: 0})
    else:
        dict_final[a] += 1
    print(dict_final)


# TASK 2

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = dict()

for a in stock:
    total_price.update({a: stock[a]*prices[a]})

print (total_price)

# TASK 3

a = [(x, x**2) for x in range(1, 11)]
print(a)

# TASK 4

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
dict1 = dict()
dict2 = dict()

for i in range(len(days)):
    dict1.update({i+1: days[i]})
    dict2.update({days[i]: i+1})
print(dict1, dict2, sep = '\n')
