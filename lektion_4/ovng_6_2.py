# Läs in texten från användaren
text = input("Ange en text: ")

# Läs in bokstaven som ska räknas
bokstav = input("Ange bokstav: ")

# Gör jämförelsen skiftlägeskänslig genom att konvertera både texten och bokstaven till små bokstäver
text = text.lower()
bokstav = bokstav.lower()

# Initialisera en räknare för att hålla reda på antalet förekomster av bokstaven
antal_forekomster = 0

# Iterera genom texten med en while-loop
index = 0
while index < len(text):
    # Om det aktuella tecknet i texten är lika med den angivna bokstaven, öka räknaren
    if text[index] == bokstav:
        antal_forekomster += 1
    index += 1

# Skriv ut resultatet
print(f"Bokstaven {bokstav} förekommer {antal_forekomster} gånger i texten.")
