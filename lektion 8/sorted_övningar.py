persons = ["Alice","Lucas","Olivia","Liam","Astrid","William"]
sorted_persons = sorted(persons)

with open("Present","w") as file:
    for person in sorted_persons:
        file.write("[ ]" + person + "\n")
