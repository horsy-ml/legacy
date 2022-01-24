import json


def get_auth():
    with open('config.cfg') as f:
        config = json.load(f)

    try:
        if config['auth']:
            return config['auth']
        else:
            raise Exception('No auth found')
    except:
        print('[!] No auth found, please login first')
        print('email')
        email = input('> ')
        print('password')
        password = input('> ')
        config['auth'] = {'email': email, 'password': password}
        with open('config.cfg', 'w') as f:
            json.dump(config, f)
        print('[OK] Auth created')
        return config['auth']


def del_auth():
    with open('config.cfg') as f:
        config = json.load(f)
    if config['auth']:
        config['auth'] = None
        with open('config.cfg', 'w') as f:
            json.dump(config, f)
        print('[OK] Auth deleted')