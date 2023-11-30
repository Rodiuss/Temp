import json

global file_name
file_name = 'database.txt'

def read_data_from_file():
    try:
        with open(file_name, 'r', encoding='UTF-8') as cursor:
            return json.loads(cursor.read())
    except FileNotFoundError:
        return []

def write_data_to_file(users: list):
    with open(file_name, 'w', encoding='UTF-8') as cursor:
        json.dump(users, cursor, indent=4)
