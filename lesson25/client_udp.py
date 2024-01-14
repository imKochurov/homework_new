import socket

def client():
    server_adress = ('localhost', 1234)
    my_message = 'Hello! This is my UDP client/server connection'

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        print(f'Відправляю повідомлення "{my_message}"')
        sender = client_socket.sendto(my_message.encode(), server_adress)

        print('Очікую відповідь...')
        data, server = client_socket.recvfrom(2048)
        print(f'Отримано {len(data)} байт від {server}')
        print(f'Отримані дані: "{data.decode()}"')

if __name__ == '__main__':
    client()