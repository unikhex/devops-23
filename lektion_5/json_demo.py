import json

attendants = ['Åsa','Kalle', 'Olivia', 'Johan']

with open('data.json', 'w') as f:
    f.write(json.dumps(attendants))

with open("data.json") as f:
    data = json.loads (f.read())
print(data[0])