from pprint import pprint
from ttp import ttp
import json
import time
from netmiko import ConnectHandler

ssh = {
    'device_type': 'alcatel_sros',
    'ip': '135.243.92.119',
    'username': 'admin',
    'password': 'admin',
    'port': '22'
}

print ('Connection successful')

net_connect = ConnectHandler(**ssh)
output = net_connect.send_command('show port detail')
#print (output)


parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

results = parser.result(format='json')[0]

#converting str to json. 
result = json.loads(results)

#print(result[0][1]['Port_Number'])

#print(len(result[0]))

i = 0

while i < len(result[0]):
    # print(result[0][i]['Port_Number'])
    if "Port_Number" in result[0][i] and "Utilization_Input" in result[0][i] and "Utilization_Output" in result[0][i]:
        print(f"{result[0][i]['Port_Number']} --> Utilization Input degeri : {result[0][i]['Utilization_Input']} Utilization Output degeri: {result[0][i]['Utilization_Output']}")
    i = i + 1
