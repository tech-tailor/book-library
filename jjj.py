import json

dict_var = {
    'name': 'Akin',
    'Age': 32676
}

with open('file.json', 'w') as f:
    json.dump(dict_var, f, indent=2)

d = json.dumps(dict_var)

print(d)

l = json.loads(d)

print(l)