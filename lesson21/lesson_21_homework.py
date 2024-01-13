# 1. Контекстний менеджер для логування:
# Створіть контекстний менеджер, який логує час початку та завершення блоку коду.
# Після завершення блоку виведіть загальний час виконання.

import time

# Контекстний менеджер для вимірювання часу спрацювання коду:
class Time_:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, type, value, traceback):
        total_time = time.time() - self.start_time
        print(f'ЧАС ВИКОНАННЯ КОДУ: {round(total_time, 3)} секунд')

# Тест контекстного менеджера
with Time_():
    time.sleep(2)




# 2. Контекстний менеджер для роботи з файлами:
# Створіть контекстний менеджер, який автоматично відкриває та закриває файл.
# При виході з контексту забезпечте збереження змін у файлі.
    
class MyContextManager:
    def __init__(self, file_name, file_method):
        self.object = open(file_name, file_method)
    def __enter__(self):
        return self.object
    def __exit__(self, type, value, traceback):
        self.object.close


with MyContextManager('lesson21/con_manager_test.txt', 'w') as file:
    file.write('Hello! This is MyContextManager test.')