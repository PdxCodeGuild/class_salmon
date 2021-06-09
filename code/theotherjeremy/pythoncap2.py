# ______________________- to veryify
import requests
data = {'grant_type': 'client_credentials', 'scope': 'product.compact'}
headers = {'accept': 'application/json', 'Authorization': 'Basic Y2hlY2tlci05YmNmMGVkYzc1OTQ0YjI2MGRlODI3OWQ3YTZkODE3NDYwNjcxNzAxMzE5NTQzNDIyMTY6Qm9zTWRlWXVHS2NRSm95T0Y1SnladVJlbG9pY2g2MGtldHZ3Q3Z0Ug==',
           'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.post(
    'https://api-ce.kroger.com/v1/connect/oauth2/token', headers=headers, data=data)
response2 = response.text

print(response2['access_token'])
