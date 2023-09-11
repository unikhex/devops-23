# creates a dictionary
person = {
    "name": "Mahmud",
    "age": "50",
}
"""
# calls the element
print(person['name'])
print(person['age'])

print(F"Hej! Jag heter {person['name']}!")
print(F"Jag  {person['age']} år gammal. ")

# Referera mot en nyckel dynamiskt
attr = input('Ange attribut (nyckel) >')
try:
    print(person[attr])
except KeyError:
    print('FEL: Attribut existerar inte')

"""
# element modification
person['age']=  51
print(person)

# add new data
person["adress"] = "Somewhere 12"
print(person)

#remove an element
del person["age"]
print(person)

for key in person:
    print("Key", key)
    print("Value", person[key])


person["address"] = {
    "gatuadress": "somwhere 12",
    "ort" : "stockholm",
    "postnummer" : "122222"
}

print(person['address']["gatuadress"])
(print(person['address']["postnummer"]),
print(person['address']['ort']))