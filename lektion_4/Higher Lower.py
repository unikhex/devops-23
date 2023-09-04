import random
def print_separator(ui_width, char='-'):
    print(char * ui_width)

def print_centered_text(text, ui_width, char='-'):
    formatted_text = f'{char} {text} {char}'
    print(formatted_text.center(ui_width))

ui_width = 50

print_separator(ui_width)
print_centered_text('HIGHER LOWER', ui_width)
print_separator(ui_width)

start = 0
stop = 99
no_guesss = random.randint(0,99)

try:
    while True:
        guez = int(input("Guess a number between 0 - 99 : "))
        if guez < no_guesss:
            print("higher")
        elif guez > no_guesss :
            print("Lower")
        elif guez == no_guesss:
            print("You've got it")
        else:
            print("Try agin")

except ValueError:
    print("That is not a number")




