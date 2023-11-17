# TASK 1
from module_9 import func
print("Розрахуємо квадрат введеного числа.")
func()


# TASK 2

import sys
print(sys.version) # Версія Python
print(sys.path) # Переглядаємо список каталогів, де Python шукає потрібний модуль, якщо його нема серед вбудованих
directory_module = 'D:\Programming_Course\homework_new'
sys.path.append(directory_module) # Додаємо потрібну директорію для пошуку модулів
