# TASK 1

import random
computer = random.randint(1,10)
# print(computer)
user = input("Спробуйте вгадати число, яке обрав комп'ютер. Введіть число від 1 до 10: ")
if user.isdigit() == True:
    if int(user) >= 1 and int(user) <= 10:
        if int(user) == computer:
            print(f"Ви вгадали! Комп'ютер також обрав число {computer}.")
        else:
            print(f"Ви не вгадали... Комп'ютер обрав число {computer}.")
    else:
        print("Ви вказали число у неправильному діапазоні.")
else:
    print("Ви ввели не число.")

print('\n\n')

# TASK 2

name = input('Print your name: ')
age = int(input('Print your age: '))
print(f"Hello {name}, on your next birthday you’ll be {age+1} years")

print('\n\n')

# TASK 3

#import random

slovo = 'Hello'

for i in range (1,6):
  abrakadabra = random.sample(slovo,  len(slovo))
  #print(abrakadabra)
  myString = ''.join(abrakadabra)
  print(myString)
  i += 1

