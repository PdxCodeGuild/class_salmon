import requests
import json

# response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
# data = response.text
# print(data)
# # print(len(data))
# print(type(data))

# with open('response_test.json', 'w') as file:
#     file.write(data)
# print('done')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# query = json.load(open('response_json.json', 'r'))
# print(type(query))
# print(query['data'][0]['brand'])
print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ')
print('the 1st way:')
import Testing
print(Testing.variable)

print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ')
print('the 2nd way:')

from Testing import variable
# NOTE a) how nothing "runs" from Testing.py now
print(variable) # NOTE b) note how you have access to the "variable", this is what you want with secrets:
# from secrets import official
print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ')