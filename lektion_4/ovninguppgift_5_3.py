def print_separator(ui_width, char='-'):
    print(char * ui_width)

def print_centered_text(text, ui_width, char='-'):
    formatted_text = f'{char} {text} {char}'
    print(formatted_text.center(ui_width))

ui_width = 50

print_separator(ui_width)
print_centered_text('MATHLETE v2.0', ui_width)
print_separator(ui_width)

antal_tal = 0
summa = 0

while True:
    try:
        # Låt användaren mata in ett tal eller "exit" för att avsluta
        inmatning = input(" > ")

        # Om användaren skriver "exit", avsluta loopen
        if inmatning.lower() == "exit":
            break

        # Försök att konvertera inmatningen till ett heltal
        tal = float(inmatning)

        # Uppdatera antal, summa och fortsätt loopa
        antal_tal += 1
        summa += tal
    except ValueError:
        print("FEL: Ogiltigt nummer")

print("-------------------")
if antal_tal > 0:
    medelvarde = summa / antal_tal
    print(f"Kardinalitet: {antal_tal}")
    print(f"Summa: {summa}")
    print(f"Medelvärde: {medelvarde}")
else:
    print("Inga giltiga nummer matades in.")