import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position':'Software engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position':'Data engineer',
    }
]

def create_client(client):
    global clients

    if (client not in clients):
        clients.append(client)
    else:
        print('Client already is in the client list')


def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
        ))

def update_client(client_name):
    global clients

    for client in clients:
        if(client_name == client['name']):
            index = clients.index(client)
            updated_client = _get_client_from_user()
            clients[index] = updated_client
            return

    print('Client is not in the client list')

    # if(client_name in clients):
    #     index = clients.index(client_name) #Buscamos el indice dentro de la lista clients
    #     clients[index] = updated_client_name
    # else:
    #     print('Client is not in clients list')

def delete_client(client_name):
    global clients

    for client in clients:
        if(client_name == client['name']):
            clients.remove(client)
        else:
            print('Client is not in clients list')


def search_client(client_name):
    #La funcion split nos permite dividir un string en una lista
    global clients
    # for client in clients:
    #     if(client_name == client):
    #         return True
    
    for client in clients:
        if(client_name == client['name']):
            return True
    
    return False

    # for client in clients_list:
    #     if client != client_name:
    #         continue
    #     else:
    #         return True

def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def _add_comma():
    global clients
    clients += ', '


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))

    return field

def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name?')
        client_name = client_name.capitalize()

        if( client_name == 'exit'):
            client_name = None
            break

    if not client_name:
        sys.exit()
    
    return client_name




if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if(found):
            print('{} is in the client list'.format(client_name))
        else:
            print('The client: {} is not in our client list'.format(client_name))

    else:
        print('Invalid command')
