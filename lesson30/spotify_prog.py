# В ЗАВДАННІ ВИКОРИСТОВУЮ API ВІД ПЛАТФОРМИ SPOTIFY
# API ДОЗВОЛЯЄ ОТРИМАТИ РІЗНОМАНІТНУ ІНФОРМАЦІЮ ПРО МУЗИЧНИХ ВИКОНАВЦІВ
# В НАВЕДЕНОМУ КОДІ ОТРИМУЄМО АЛЬБОМИ ОБРАНОГО ВИКОНАВЦЯ ТА СПИСОК
# ІЗ СХОЖИХ ВИКОНАВЦІВ НА ОСНОВІ АНАЛІЗУ ВПОДОБАНЬ КОРИСТУВАЧІВ SPOTIFY


# import json
import spot_config # файл конфігурації з особистими данними ключів
import spotipy # додатковий встановлений модуль для роботи з платформою Spotify


# Створюємо власного клієнта для відправки запитів за документацією
CLIENT_ID = spot_config.client_id
CLIENT_SECRET = spot_config.client_secret
sp = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))


# URI-посилання на The Rolling Stones. Можна також використати формати URL або ID виконавця з платформи Spotify:
rs_URI = 'spotify:artist:22bE4uQ6baNwSHPVcDxLCe'


# Результат запиту - словник з останніх 20 альбомів The Rolling Stones в форматі {НАЗВА : РІК}
# (результат у файлі rs_albums.json):
rs_items = sp.artist_albums(artist_id=rs_URI).get('items')
rs_albums = {i.get('name'): i.get('release_date') for i in rs_items}


# Результат запиту - словник із 20 схожих на The Rolling Stones виконавців {НАЗВА ВИКОНАВЦЯ : РЕЙТИНГ},
# відсортовані за рейтингом Spotify (результат у файлі related_artists.json):
rs_related = sp.artist_related_artists(artist_id=rs_URI).get('artists')
related_artists = {i.get('name'): i.get('popularity') for i in rs_related}
convert = sorted(related_artists.items(), key=lambda x:x[1], reverse=True)
related_artists_sorted = dict(convert)







# Запис результатів у файл для зручності перегляду
# with open('SPOTIFY/rs_albums.json', 'w') as file:
#     json.dump(rs_albums, file, indent=2)

# print(rs_albums)