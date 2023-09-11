import json

article = {
    "before trip": "pack clothes",
}

def print_separator(ui_width, char='-'):
    print(char * ui_width)

def print_centered_text(text, ui_width, char='-'):
    formatted_text = f'{char} {text} {char}'
    print(formatted_text.center(ui_width))

ui_width = 50

print_separator(ui_width)
print_centered_text('ALWAYS NOTE', ui_width)
print_separator(ui_width)

print_separator(ui_width)
print_centered_text('Current Articles', ui_width)
print_separator(ui_width)

for key, value in article.items():
    print(f"- {key}\n  {value}\n")

add_article = input("Add a title to your article: ").lower()
add_text = input("Explain why that was added: ").lower()

article[add_article] = add_text
for key, value in article.items():
    print(f"- {key}\n  {value}\n")

# Save the updated article to a JSON file
with open("articles.json", "w") as file:
    json.dump(article, file)
