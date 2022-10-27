from random import choice
from log_decorator import log_decorator


def create_data_clients(number_of_clients: int) -> dict:
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'

    clients = {}
    for i in range(1, number_of_clients + 1):
        name = ''.join([choice(ascii_uppercase) if i == 0 else choice(ascii_lowercase) for i in range(10)])
        phone = ''.join([choice(digits) for _ in range(8)])
        id_client = str(i)
        clients[id_client] = {'name': name, 'phone': phone}

    return clients


def create_data_file(clients: dict) -> None:
    with open('bd', 'wt+') as file:
        file.writelines('{} : {} \n'.format(id_client, value) for id_client, value in clients.items())


@log_decorator
def main(number_of_create_clients=1000000):
    clients = create_data_clients(number_of_create_clients)
    create_data_file(clients)


if __name__ == '__main__':
    main()
