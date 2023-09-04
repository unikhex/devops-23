choice_start = int(input("Choose a start number: "))
choice_stop = int(input("Choose a number to stop at: "))
choice_increment = int(input("Choose a number to increase with: "))

for n in range(choice_start, choice_stop, choice_increment):
    print(n)