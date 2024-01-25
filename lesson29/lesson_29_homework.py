# АСИНХРОННІСТЬ
# Виконаємо наступну задачу: отримаємо по API-запиту кількість втрат противника за певну дату
# Далі будемо створювати запити для списку дат - по запиту на кожну дату
# Спочатку подивимося на результати для звичайного виконання коду,
# потім використаємо асинхронний підхід для створення одночасних запитів по списку дат

import asyncio
import aiohttp
from lesson21.lesson_21_homework import Time_
import requests

# Функція повертає кількість втрат противника за визначену дату

def day_(date:str):
    url_api = 'https://russianwarship.rip/api/v2'
    statistics = f'/statistics/{date}'
    obj = requests.get(url_api + statistics)
    result = obj.json()
    get_units_today = result.get('data').get('increase').get('personnel_units')
    return get_units_today

# Функція повертає словник із кількості втрат противника по списку введених дат

dates = ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06']

def period_(dates:list):
    res = {}
    for date in dates:
        res.update({date: day_(date)})
    return res

# Перевіряємо час роботи функцій

with Time_():
    print(f'Запит по одній даті {dates[2]}. Кількість втрат противника: {day_(dates[2])}')

with Time_():
    print('\nЗвичайний запит:', period_(dates))

# РЕЗУЛЬТАТИ ЧАСУ ЗАПИТІВ:

    # Запит по даті 2024-01-03.
    # Кількість втрат противника: 680
    # ЧАС ВИКОНАННЯ КОДУ: 0.252 секунд
        
    # {'2024-01-01': 780, '2024-01-02': 810, '2024-01-03': 680, '2024-01-04': 780, '2024-01-05': 790, '2024-01-06': 800}
    # ЧАС ВИКОНАННЯ КОДУ: 10.259 секунд

# ВИКОРИСТАЄМО АСИНХРОННИЙ ПІДХІД:

async def main(dates):
    url_api = 'https://russianwarship.rip/api/v2'
    result_dict = {}
    async with aiohttp.ClientSession() as session:
        for date in dates:
            date_url = url_api + f'/statistics/{date}'
            async with session.get(date_url) as resp:
                statistic_date = await resp.json()
                result = statistic_date.get('data').get('increase').get('personnel_units')
                result_dict.update({date: result})
    return result_dict

with Time_():
    print('\nАсинхронний запит:', asyncio.run(main(dates=dates)))

# РЕЗУЛЬТАТ:

    # Запит по одній даті 2024-01-03. Кількість втрат противника: 680
    # ЧАС ВИКОНАННЯ КОДУ: 0.253 секунд

    # Звичайний запит: {'2024-01-01': 780, '2024-01-02': 810, '2024-01-03': 680, '2024-01-04': 780, '2024-01-05': 790, '2024-01-06': 800}
    # ЧАС ВИКОНАННЯ КОДУ: 1.606 секунд

    # Асинхронний запит: {'2024-01-01': 780, '2024-01-02': 810, '2024-01-03': 680, '2024-01-04': 780, '2024-01-05': 790, '2024-01-06': 800}
    # ЧАС ВИКОНАННЯ КОДУ: 0.432 секунд

# ОТЖЕ, В АСИНХРОННОМУ ВАРІАНТІ МАЄМО МАЙЖЕ В 4 РАЗИ МЕНШИЙ ЧАС ВИКОНАННЯ API-ЗАПИТІВ ДЛЯ СПИСКУ ВИЗНАЧЕНИХ ДАТ


# Джерело: https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp