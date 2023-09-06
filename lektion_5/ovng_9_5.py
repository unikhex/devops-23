def print_separator(ui_width, char='-'):
    print(char * ui_width)

def print_centered_text(text, ui_width, char='-'):
    formatted_text = f'{char} {text} {char}'
    print(formatted_text.center(ui_width))

ui_width = 50

print_separator(ui_width)
print_centered_text('STACK MASTER', ui_width)
print_separator(ui_width)
cars = ["mercedes", "volvo","toyota"]
print("What we have\n",cars)
print("push --> to add")
print("pull -->to remove")

ask = input("Do you want to do (push/pull) :").lower()
if ask == "push":
    add_sth = input("Add something")
    cars.append(add_sth)
    print("Here is the updates list", cars)
elif ask == "pull":
    remove_sth = input("What do you wish to remove: ")
    cars.remove(remove_sth)
    print("Here is the updated list", cars)
else:
    print("Ok then. There is nothing for you here")
