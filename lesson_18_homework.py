# TASK 1 (LMS)

class Email:
    def __init__(self, e_mail:str):
        self.e_mail = e_mail
        self.domens_list = ['gmail.com', 'ukr.net', 'protonmail.com']
        print(self.validate()) # викликаємо метод validate() в методі __init__ відповідно до умови завдання

    def validate(self):
        if '@' in self.e_mail:
            verify = self.e_mail.rsplit('@')
            if verify[0].isalnum() and any(domen == verify[1] for domen in self.domens_list): # перевіряємо, щоб e-mail складався лише з букв і літер та належав до переліку дозволених доменів
                return f'e-mail "{self.e_mail}" is validate'
            else:
                return f'e-mail "{self.e_mail}" is not validate'


a = Email('abc789@gmail.com')

# TASK 2 (LMS)

class Boss:
    def __init__(self, id:int, name:str):
        self._id = id
        self._name = name
        self._workers_list = []

    @property
    def workers(self):
        return self._workers_list
    
    def add_worker(self, worker):
        if isinstance(worker, Worker) and worker.boss is None: # додаємо Працівника в список Керівнику, якщо в працівника ще немає Керівника
            self._workers_list.append(worker)
            worker.boss = self # в екземплярі Працівника через сетер призначаємо йому цього Босса

class Worker:
    def __init__(self, id:int, name:str):
        self._id = id
        self._name = name
        self._boss = None

    @property
    def boss(self):
        return self._boss
    
    @boss.setter
    def boss(self, add_boss):
            self._boss = add_boss



boss1 = Boss(1, 'Катерина')
boss2 = Boss(2, 'Андрій')

worker1 = Worker(1, 'Володимир')
worker2 = Worker(2, 'Ганна')

# в прінтах звертаюся до protected-змінних просто для швидкої візуалізації, щоб не писати зайві геттери

print(f'\nКерівник у {worker1._name}: {worker1.boss}, керівник у {worker2._name}: {worker2.boss}')
print(f'Список працівників у {boss1._name}: {boss1.workers}, cписок працівників у {boss2._name}: {boss2.workers}')

boss1.add_worker(worker1)
boss2.add_worker(worker2)

print(f'\nКерівник у {worker1._name}: {worker1.boss._name}, керівник у {worker2._name}: {worker2.boss._name}')
print(f'Список працівників у {boss1._name}: {[worker._name for worker in boss1.workers]}, cписок працівників у {boss2._name}: {[worker._name for worker in boss2.workers]}')

# Але лишилися питання: в моєму варіанті, якщо закріпити працівника за керівником, керівника вже не зміниш,
# або принаймні в екземплярі працівника ми змінимо боса, але він лишиться в списку працівників в екземплярі минулого керівника.

# Я мучався і не домучив варіант, щоб додаючи одному із босів працівника, він автоматично видалявся із списку працівників минулого боса, якщо він там був
# Зрозуміло, треба змінити умову if на 33 рядку і прибрати None, але треба ще якось залізти в екземляр минулого боса і видалити працівника з того списку 

# TASK 3 (LMS)

class TypeDecorators:
    def to_bool(func):
        def wrapper(*args):
            result = func(*args)
            return bool(result)
        return wrapper
    
    def to_list(func):
        def wrapper(*args):
            result = func(*args)
            return [result]
        return wrapper
        
    def to_dict(func):
        def wrapper(*args):
            result = func(*args)
            return {'result': result}
        return wrapper

@TypeDecorators.to_dict
def to_str(number):
    return str(number)

@TypeDecorators.to_bool
def to_int(number):
    return int(number)

@TypeDecorators.to_list
def to_float(number):
    return float(number)

print('\n', to_str(25), to_int(25), to_float(25), sep='\n')


# TASK 2 (Slack, optional)

# Створіть дескриптор DiscountLimit, який визначає максимальний обсяг знижки для товару.
# Забороніть встановлення знижки більше, ніж встановлено за лімітом.


class Descriptor:
    def __init__(self, max_discount):
        self.max_discount = max_discount

    def __set__(self, instance, value):
        if value > self.max_discount:
            raise ValueError(f"Discount can't be higher than {self.max_discount}")


class Product:
    limit_discount = Descriptor(max_discount=15)

    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def discount(self, discount):
        self.limit_discount = discount
        self.price = self.price*(1 - discount/100)
        return f'Price with discount: {self.price}'
    
product1 = Product('smartphone', 15000)

print(product1.discount(15))