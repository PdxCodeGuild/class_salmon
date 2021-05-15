
import json

# with open(r'C:\Users\flux\programs\class_eagle\1 Python\solutions\data\todo.json', 'r') as file:
with open('./data/todo.json', 'r') as file:
    text = file.read()
print(text)

data = json.loads(text)
print(data)

for todo in data['todos']:
    print(todo['text'])

data['todos'].append({
    'text': 'buy groceries',
    'priority': 'medium'
})

with open('./data/todo.json', 'w') as file:
    data_json = json.dumps(data, indent=4)
    file.write(data_json)



