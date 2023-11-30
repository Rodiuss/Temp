from user_management import *

def main():
    m_string = '\n1. Register\n'\
            '2. Log in\n'\
            '3. Update account\n'\
            '4. Delete an account\n'\
            '5. Exit\n'\
            '-> '

    while True:
        match input(m_string):
            case '1':
                register_user()
            case '2':
                login_user()
            case '3':
                update_user()
            case '4':
                delete_user()
            case '5':
                break
            case _:
                print('Invalid command!')

if __name__ == '__main__':
    main()
