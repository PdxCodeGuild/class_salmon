
contacts = [{
    'id': 1
},{
    'id': 2
},{
    'id': 4
}]

max_id = max(contacts, key=lambda x: x['id'])
print(max_id['id'])

