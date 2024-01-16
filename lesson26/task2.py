import json
import requests

url_api = 'https://russianwarship.rip/api/v2'
date = '2024-01-16'

def war_info(): # Загальна інформація про стан війни
    info = '/war-info'
    obj = requests.get(url_api + info)
    result = obj.json()
    return result

with open('lesson26/war.json', 'w') as file: # Записуємо наш запит в JSON-файл
    json.dump(war_info(), file, indent=2)


def stat(date): # Загальна статистика. Вибираємо, який день війни, загальні втрати живої сили противника за весь час і за останню добу.
    statistics = f'/statistics/{date}'
    obj = requests.get(url_api + statistics)
    result = obj.json()
    day = result.get('data').get('day')
    get_units_total = result.get('data').get('stats').get('personnel_units')
    get_units_today = result.get('data').get('increase').get('personnel_units')
    return f'\nСтаном на {date} йде {day} день війни.\nЗагальні втрати ворога - {get_units_total} осіб.\nЗа останню добу - {get_units_today} осіб.'

print(war_info())
print(stat(date=date))
