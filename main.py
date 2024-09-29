from simple_salesforce import Salesforce
import pandas as pd
from datetime import datetime
from decouple import config

# Conexion con Salesforce

username = config('USERNAME_SF')
password = config('PASSWORD_SF')
token = config('TOKEN_SF')

sf = Salesforce(username=username,password=password,security_token=token)
print(sf)

response = sf.query("SELECT Id, Name, Type, Zone__c, Province__c "
                    "FROM Account "
                    "WHERE Zone__c = 'Centro'")
#print(response)
#print(response['records'])
#print(response['totalSize'])

#for i in response['records']:
#    print(i)

for i in response['records']:
    print(f"ID: {i['Id']}, Name: {i['Name']}")

df = pd.DataFrame(response['records'])
pd.set_option('display.max_columns', 100)
pd.set_option('expand_frame_repr', True)
#print(df)

fileInfo = {
    "Name":"Prueba desde Python version 3",
    "Type": "Market",
    "Zone__c" : "Centro",
    "Province__c" : "Zaragoza"
}

acct : sf.Account.create(fileInfo)

current_timestamp = datetime.now()
df.to_csv("{0}_sfdc_data.csv".format(current_timestamp.strftime("%Y-%m-%d")), index=False)


