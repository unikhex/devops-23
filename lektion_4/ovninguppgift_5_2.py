def print_separator(ui_width, char='-'):
    print(char * ui_width)

def print_centered_text(text, ui_width, char='-'):
    formatted_text = f'{char} {text} {char}'
    print(formatted_text.center(ui_width))

ui_width = 50

print_separator(ui_width)
print_centered_text('THE GREAT DIVIDER', ui_width)
print_separator(ui_width)

try:
    while True:
        no_1 = float(input("Give me a number : " ))
        no_2 = float(input("Give another number : "))
        if no_2 == 0:
            break
        res_ult = no_1 / no_2
        print(res_ult)

except ValueError:
    print("That is not a number")