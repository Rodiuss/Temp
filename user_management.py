from file_handling import *

def get_info(msg, cnt):
    while (result := input(msg).strip().split()) or True: 
        if len(result) == cnt:
            return result
        else:
            print('Incorrect input!')

def register_user():
    users = read_data_from_file()
    row_data = get_info('Enter name, surname, email, and password: ', 4)
    user = {'name': row_data[0], 'surname': row_data[1], 'email': row_data[2], 'password': row_data[3]}

    if user['email'] in [user["email"] for user in users]:
        print('Email already exists!')
        return
    
    users.append(user)
    write_data_to_file(users)
    print('User added!')

def login_user():
    row_data = get_info('Enter your email and password: ', 2)

    for user in read_data_from_file():
        if user['email'] == row_data[0] and user['password'] == row_data[1]:
            print(f'Hello, {user["name"]}')
            return
    else:
        print('Incorrect data!')

def update_user():
    row_data = get_info('Enter your email and password: ', 2)
    users = read_data_from_file()
    
    for user in users:
        if user['email'] == row_data[0] and user['password'] == row_data[1]:
            new_row_data = get_info('Enter new name, surname, email, and password: ', 4)
            
            user['name'] = new_row_data[0]
            user['surname'] = new_row_data[1]
            user['email'] = new_row_data[2]
            user['password'] = new_row_data[3]
            
            write_data_to_file(users)
            print('Account updated!')
            return
    else:
        print('Incorrect data!')

def delete_user():
    row_data = get_info('Enter your email and password: ', 2)
    users = read_data_from_file()

    for user in users:
        if user['email'] == row_data[0] and user['password'] == row_data[1]:
            users.remove(user)
            write_data_to_file(users)
            print('Account deleted!')
            return
    else:
        print('Incorrect data!')

