# TASK 1 (LMS)
# Створіть власну реалізацію вбудованої функції enumerate з назвою 'with_index',
# яка приймає два параметри: 'iterable' і 'start', за замовчуванням 0.

class My_enumerate_custom:
    def __init__(self, iter_object, start_value):
        self.obj = iter_object
        self.start = start_value
        self.obj_start = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.obj_start < len(self.obj):
            cnt = self.start
            value = self.obj[self.obj_start]
            self.obj_start += 1
            self.start += 1
            return cnt, value
        else:
            raise StopIteration

l1 = ["abc", "bcd", "cde", "xyz"]
obj1 = enumerate(l1, 3)
obj2 = My_enumerate_custom(l1, 3)
print(list(obj1), list(obj2), sep='\n')

# TASK 2 (LMS)
# Створіть власну реалізацію вбудованої функції range,
# яка приймає три параметри:'start', 'end' і необов'язковий крок.

class My_range_custom:
    def __init__(self, *args):
        num_args = len(args)
        if num_args == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif num_args == 2:
            self.start, self.stop = args
            self.step = 1
        elif num_args == 3:
            self.start, self.stop, self.step = args
            if self.step == 0:
                raise ValueError('"Step" must not be zero')
        else:
            raise TypeError(f"'My_range_custom' takes 3 arguments, not {num_args}")

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < self.stop:
            value = self.start
            self.start += self.step
            return value
        else:
            raise StopIteration

a = range(1, 20, 2)
b = My_range_custom(1, 20, 2)
print(list(a), list(b), sep='\n')

# TASK 3 (LMS)
# Створіть власну реалізацію ітератора, який можна використовувати всередині циклу for-in.
# Також додайте логіку для отримання елементів за допомогою синтаксису квадратних дужок.


### Вбудована функція range має можливість доступу до елементів за їх індексом. Я не врахував цю можливість в попередньому завданні.
### Тож, для виконання умови Завдання 3, розширимо функціонал коду із попереднього Завдання 2

class My_range_custom3:
    def __init__(self, *args):
        num_args = len(args)
        if num_args == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif num_args == 2:
            self.start, self.stop = args
            self.step = 1
        elif num_args == 3:
            self.start, self.stop, self.step = args
            if self.step == 0:
                raise ValueError('"Step" must not be zero')
        else:
            raise TypeError(f"'My_range_custom' takes 3 arguments, not {num_args}")

    def __iter__(self):
        return self
    
    def __next__(self): # на відміну від попередньої реалізації, розширюємо функціонал і для від'ємних послідовностей
        if self.start < self.stop and self.step > 0:
            value = self.start
            self.start += self.step
            return value
        elif self.start > self.stop and self.step < 0:
            value = self.start
            self.start += self.step
            return value
        else:
            raise StopIteration
        
    def __getitem__(self, key):
        if key >= 0: # для отримання елементу за додатнім індексом (з початку послідовності)
            result = self.start + self.step*key
            return result
        elif key < 0: # для отримання елементу за від'ємним індексом (з кінця послідовності)
            result = self.stop + self.step*key
            return result
    

a1 = range(100, 50, -2)
b1 = My_range_custom3(100, 50, -2)

print(a1[-2], b1[-2], sep='\n')

# використовуємо послідовність в циклі FOR відповідно до завдання:
c = [ i for i in b1]
print(c)