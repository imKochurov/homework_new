import requests

url_list = ['https://en.wikipedia.org', 'https://twitter.com'] # Перелік сайтів
directory = 'lesson26' # Директорія, куди записуємо файли

def get_robots(links): # Функція створення об'єктів HTML запиту.
    add_ = '/robots.txt'
    result = [requests.get(i + add_) for i in links]
    return result

def writing_files(directory, links): # Функція запису у файли файлів robots.txt у форматі file1.txt, file2.txt...
    objects = get_robots(links=links)
    for i in objects:
        with open(f'{directory}/file{objects.index(i) + 1}.txt', 'w', encoding='utf-8') as file:
            file.write(i.text)

if __name__ == '__main__':
    writing_files(directory=directory, links=url_list)