def main():
    # Skapa en lista för att lagra de inmatade heltalen
    numbers = []

    # Be användaren mata in fem heltal
    for i in range(5):
        try:
            number = int(input(f"Mata in heltal {i+1}: "))
            numbers.append(number)
        except ValueError:
            print("Ogiltigt inmatning. Försök igen.")

    # Använd den inbyggda funktionen max för att hitta det högsta talet
    highest_number = max(numbers)

    # Presentera det högsta talet för användaren
    print(f"Högsta talet är: {highest_number}")

if __name__ == "__main__":
    main()

#This was not done by me lol