person = {
    "firstname": "Johan",
    "lastname": "Svensson",
    "age": 25,
    "pets": [
    {"name": "Morris","age": 3,"typ": "dog"},
    {"name": "Lisa","age": 4,"typ": "cat"}
    ]
}
namn = person['firstname'] + " " + person['lastname']
age = person['age']
count_pets = len((person['pets']))

print('....ÖVNING......')
print(f"{namn} är {age} år gammal och har {count_pets} husdjur")


for pet in person['pets']:
    print(f"* En {pet['age']} gammal {pet['typ']} som heter {pet['name']}")