registered = ["Anna", "Eva ","Erik","Lars","Karl"]
absent = ["Anna", "Erik","Karl"]

for person in absent:
    if person in registered:
        registered.remove(person)

print(registered)

