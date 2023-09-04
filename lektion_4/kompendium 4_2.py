def print_multiplication_table(number, limit):
    print(f"Multiplication table for {number}:")
    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

while True:
    try:
        number = int(input("Enter a number (or a negative number to quit): "))
        if number < 0:
            break

        limit = 3  # Display multiplication table up to the first 3 multiples
        print_multiplication_table(number, limit)

        # Ask if the user wants to see more tables
        continue_choice = input("Do you want to see more tables? (yes/no): ").strip().lower()
        if continue_choice != "yes":
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Thank you for using the multiplication table generator!")
