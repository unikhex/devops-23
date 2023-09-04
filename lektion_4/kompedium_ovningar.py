def print_separator(ui_width, char='-'):
    print(char * ui_width)

def print_centered_text(text, ui_width, char='-'):
    formatted_text = f'{char} {text} {char}'
    print(formatted_text.center(ui_width))

ui_width = 50

numbers = []

print_separator(ui_width)
print_centered_text('NUMBER SUM & AVERAGE CALCULATOR', ui_width)
print_separator(ui_width)

while True:
    number = int(input("Enter a number (or a negative number to stop): ".center(ui_width)))

    if number < 0:
        break  # Exit the loop if a negative number is entered

    numbers.append(number)

# Calculate the sum and average of the entered numbers
if numbers:
    total = sum(numbers)
    average = total / len(numbers)
    print_separator(ui_width)
    print("Entered numbers:".center(ui_width))
    print(numbers)
    print_separator(ui_width)
    print("Sum of numbers:".center(ui_width))
    print(total)
    print_separator(ui_width)
    print("Average of numbers:".center(ui_width))
    print(average)
    print_separator(ui_width)
else:
    print("No numbers were entered.".center(ui_width))
