import json
from pprint import pprint

with open('bk_active/ch3/Config.json', encoding='utf-8') as Json_file:
    json_data = json.loads(Json_file.read())
    
print(json_data)
pprint(json_data)
Json_file.close()

SRV_HOST_IP = json_data['HOST_IP']
SRV_HOST_PORT = json_data['HOST_PORT']
LOG_LEVEL = json_data['LOG_LEVEL']
SRV_ADMIN = json_data['SRV_ADMIN']
SRV_EMAIL = json_data['SRV_EMAIL']

print(SRV_HOST_IP)
print(SRV_HOST_PORT)
print(LOG_LEVEL)
print(SRV_ADMIN)
print(SRV_EMAIL)
