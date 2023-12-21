from datetime import datetime
import json
import unittest

# # MY FUNC:

# def func_sum(a, b):
#     return a+b

# def number_check(a:int):
#     if a%2 == 0:
#         return "Число парне"
#     else:
#         return "Число непарне"
    
# def max_value(a:list):
#     return max(a)

# # TESTS:

# def test_func_sum(func_):
#     assert func_(3, 5) == 8
#     assert func_(-3, -5) == -8
#     assert func_(-5, 5) == 0

# test_func_sum(func_sum)

# def test_number_check(func_):
#     assert func_(5) == "Число непарне"
#     assert func_(4) == "Число парне"
#     for i in range(2, 100, 2):
#         assert func_(i) == "Число парне"
#     for i in range(1, 99, 2):
#         assert func_(i) == "Число непарне"
    
# test_number_check(number_check)

# def test_max_value(func_):
#     assert func_([100, 54, 17, 111]) == 111
#     assert func_([-100, -54, -14, -111]) == -14

# test_max_value(max_value)


            # Система обліку запасів:
            # Створіть функцію, яка дозволяє додавати товари до системи обліку запасів,
            # відстежує кількість товарів та повертає інформацію про наявність товарів на складі.
###
all_goods = {}
def accounting_goods(name:str, count:int):
    all_goods.update({name: count})
    return f"Наявні товари: {[[i, all_goods.get(i)] for i in all_goods if all_goods.get(i) > 0]}"
###

            # 3. Обчислення вартості доставки:
            # Напишіть функцію, яка приймає вагу товару та відстань до місця доставки
            # і обчислює вартість доставки згідно з заданими тарифами.

###
def delivery_cost(weight, distance):
    minimal_cost = 30
    weight_coef = 3
    distance_coef = 4

    if weight > 0 and distance > 0:
        result = minimal_cost + weight*weight_coef + distance*distance_coef
        return result
    else:
        raise ValueError('"Weight" and "Distance" must be greater than zero')
###  
    
            # Автоматизація операцій з банківським рахунком:
            # Створіть функції для переведення грошей між рахунками, перевірки балансу та виведення історії транзакцій.
    
###
class Bank_Account:
    def __init__(self, id, username, amount=0):
        self.id = id
        self.username = username
        self.amount = amount

    # @property
    # def amount(self):
    #     return self.amount
    
account1 = Bank_Account('001', 'ANNA')
account2 = Bank_Account('002', 'JOHN')
account3 = Bank_Account('003', 'JACK')

class Transactions:
    with open("transaction.json", "r") as history_tr:
        transactions_ = json.load(history_tr)
    
    def put_money(self, account, money:int):
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
        if account.id not in self.transactions_ and money >= 0:
            self.transactions_.update({account.id:{'total_sum': money, 'history': {time: f'Replenished by {money} UAH'}}})
            with open("transaction.json", "w") as file:
                json.dump(self.transactions_, file, indent=2)

        elif account.id in self.transactions_ and money > 0:
            self.transactions_[account.id]['total_sum'] += money
            self.transactions_[account.id]['history'].update({time: f'Replenished by {money} UAH'})
            with open("transaction.json", "w") as file:
                json.dump(self.transactions_, file, indent=2)

Transactions().put_money(account1, 10)


# with open("transaction.json", "w") as file:
#     json.dump({}, file)



###

class Test(unittest.TestCase):
    def test_add_new(self):
        accounting_goods('name3', 0)
        self.assertIn('name3', all_goods)

    def test_result(self):
        accounting_goods('name1', 3)
        accounting_goods('name3', 0)
        result = accounting_goods('name2', 2)
        self.assertEqual(result, "Наявні товари: [['name1', 3], ['name2', 2]]")

    def test_valid_cost(self):
        self.assertEqual(delivery_cost(1, 1), 37)
        self.assertEqual(delivery_cost(2, 2), 44)
        self.assertEqual(delivery_cost(3, 3), 51)

    def test_valid_zero(self):
        with self.assertRaises(ValueError):
            delivery_cost(0, 5)
        with self.assertRaises(ValueError):
            delivery_cost(5, 0)

    
if __name__ == '__main__':
    unittest.main()