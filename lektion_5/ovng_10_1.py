# Funktion för att skriva ut vägskylten
def print_sign(current_message):
    print("|-----------------------|")
    print(f"| Welcome to {current_message} |")
    print("|-----------------------|")
    print("| C | Change sign message")
    print("| E | Exit program")
    print("|-----------------------|")
    print("| >")

# Ladda meddelandet från filen sign.txt
def load_message():
    try:
        with open("sign.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Västerås"

# Spara meddelandet till filen sign.txt
def save_message(message_to_save):
    with open("sign.txt", "w") as file:
        file.write(message_to_save)

# Huvudprogram
current_message = load_message()

while True:
    print_sign(current_message)
    choice = input("Select an option (C/E): ").upper()

    if choice == "C":
        new_message = input("Enter the new sign message: ")
        save_message(new_message)
        current_message = new_message
    elif choice == "E":
        break
    else:
        print("Invalid option. Please select 'C' or 'E'.")
