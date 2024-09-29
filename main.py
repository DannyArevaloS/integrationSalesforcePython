from simple_salesforce import Salesforce
import pandas as pd
from datetime import datetime
from decouple import config

# Conexion con Salesforce

username = config('USERNAME_SF')
password = config('PASSWORD_SF')
token = config('TOKEN_SF')

sf =Salesforce(username=username, password=password, security_token=token)
res = sf.query("SELECT Id, Name, Type FROM Account WHERE Type = 'Suppliers'")

for i in res['records']:
    print(f"ID: {i['Id']}, TYPE: {i['Type']}, NAME: {i['Name']}")

df = pd.DataFrame(res['records'])
pd.set_option('display.max_columns', 100)
pd.set_option('expand_frame_repr', True)

current_timestamp =datetime.now()


