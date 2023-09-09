# Skapa en lista med konsonanter som ska översättas
konsonanter = "bcdfghjklmnpqrstvwxyz"

# Läs in texten från användaren
text = input("Skriv in en text: ")

# Skapa en tom sträng för att hålla den översatta texten
oversatt_text = ""

# Iterera genom varje tecken i den inmatade texten
for tecken in text:
    # Om tecknet är en konsonant, lägg till ett 'o' och samma konsonant igen
    if tecken.lower() in konsonanter:
        oversatt_text += tecken + 'o' + tecken
    else:
        oversatt_text += tecken  # Annars lägg till tecknet som det är

# Skriv ut den översatta texten
print("\nRobber Translate")
print("----------------")
print(f"Svenska < {text}")
print(f"Rövarspråk > {oversatt_text}")
