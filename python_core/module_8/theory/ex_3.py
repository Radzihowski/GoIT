import json

data = {
    'developer':
        {
            'name': 'Сергій',
            'position': 'Senior Developer'
        }
}

with open('data_user.json', 'w', encoding='utf-8') as file:
    json.dump(data, f, ensure_ascii=False)

with open('data_user.json', r) as f:
    restored_data = json.load(f)
    print(restored_data)