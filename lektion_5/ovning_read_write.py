attendants = ["Lisa", "Kalle", "Olivia", "Johan"]

with open ("text.file", "w") as f:
    for attendant in attendants:
        f.write("Hello " + attendant + "!\n")