import configparser

config = configparser.ConfigParser()

config.read('bk_active/ch3/Config.ini')

SRV_ADMIN = config.get('ADMIN', 'SRV_ADMIN')
SRV_EMAIL = config.get('ADMIN', 'SRV_EMAIL')
SRV_HOST_IP = config.get('SERVER', 'HOST_IP')
SRV_HOST_PORT = config.get('SERVER', 'HOST_PORT')
LOG_LEVEL = config.get('SERVER', 'LOG_LEVEL')

print(SRV_ADMIN)
print(SRV_EMAIL)
print(SRV_HOST_IP)
print(SRV_HOST_PORT)
print(LOG_LEVEL)
