def get_input(prompt = ''):
    try:
        line = raw_input(prompt)
    except NameError:
        line = input(prompt)
    return line

#Prompts for, and returns, a username and password...
def get_credentials():
    username = get_input('Enter username: ')
    password = None
    while not password:
        password = getpass()
        password_verify = getpass('Retype your password: ')
        if password != password_verify:
            print('password do not match, try again..')
            password = None
    return username, password

username, password = get_credentials()
