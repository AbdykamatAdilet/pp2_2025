import configparser

def load_config():
    config = configparser.ConfigParser()
    config.read('database.ini')
    return {
        'host': config['postgresql']['host'],
        'database': config['postgresql']['database'],
        'user': config['postgresql']['user'],
        'password': config['postgresql']['password'],
    }