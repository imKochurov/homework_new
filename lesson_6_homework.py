# TASK 1

import random

a = []
while len(a) <= 9:
    rnd = random.randint(0, 100)
    a.append(rnd)
    
print(a, f'Максимальне значення зі списку: {max(a)}', sep = '\n')

print('\n\n')

# TASK 2

#import random

a = []
b = []
while len(a) <= 9: # в циклі генеруємо два списки по 10 випадкових символів
    rnd = random.randint(0, 10)
    a.append(rnd)
    rnd1 = random.randint(0, 10)
    b.append(rnd1)

a1 = set(a) # переводимо список в множину для уникнення дублів
b1 = set(b) # те саме
c = list(a1.intersection(b1)) # виявляємо однакові значення в множинах та переводимо множину в список

print(a, b, f'Спільні значення без дублів: {c}', sep = '\n')

print('\n\n')

# TASK 3

a = list(range(1, 101))
cnt = 0
b = []

while cnt != 100:
    if (a[cnt] % 7 == 0) and (a[cnt] % 5 != 0):
        b.append(a[cnt])
    else:
        pass
    cnt += 1

print(f'Список чисел від 1 до 100, кратних "7" і не кратних "5": ', b, sep = '\n')

print('\n')