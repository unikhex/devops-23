def print_separator(ui_width, char='-'):
    print(char * ui_width)

def print_centered_text(text, ui_width, char='-'):
    formatted_text = f'{char} {text} {char}'
    print(formatted_text.center(ui_width))

ui_width = 50

print_separator(ui_width)
print_centered_text('TODOIFY', ui_width)
print_separator(ui_width)

todos = ["Städa", "Handla", "Plugga", "Ge blod", ]
for i in todos:
    print("- " + i)
