notes = {
    "meddelande fran skolan": "Friluftsdag pa tisdag",
    "kom ihag": "Ta bilen till verkstad",
    "infortentamen": "Gör alla instuderingsuppgifter"
}

for note in notes:
    print(note)

mess = input("what do you want to know > ").lower()

if mess == "meddelande fran skolan":
    print(notes['meddelande fran skolan'])
elif mess == "kom ihag":
    print(notes['kom ihag'])
elif mess == "infortentamen":
    print(notes['infortentamen'])
else:
    print("Your input is not in the list")
