# Funktion för att rensa bort blanksteg och skiljetecken och konvertera till små bokstäver
def rensa_mening(mening):
    return ''.join(filter(str.isalpha, mening)).lower()

# Läs in den inmatade meningen
mening = input("Ange en mening: ")

# Rensa och normalisera meningen
rensad_mening = rensa_mening(mening)

# Skapa en omvänd version av den rensade meningen
omvand_mening = rensad_mening[::-1]

# Jämför den rensade meningen med dess omvända version
if rensad_mening == omvand_mening:
    print(f"'{mening}' är ett palindrom.")
else:
    print(f"'{mening}' är inte ett palindrom.")
