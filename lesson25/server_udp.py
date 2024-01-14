import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 1234))

    while True:
        print('Сервер очікує на повідомлення...')
        data, adress = server_socket.recvfrom(2048)
        print(f'Отримано {len(data)} байт від {adress}')
        print(f'Отримані дані: "{data.decode()}"')

        sender = server_socket.sendto(data, adress)
        print(f'Відправляємо назад {sender} байт за адресою {adress}')

if __name__ == '__main__':
    udp_server()
