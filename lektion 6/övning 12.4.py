article = {
    "before trip": "pack clothes",


}
print(article)

add_article = input("Add a title to your article:").lower()
add_text = input("Explain what needs why that was added:").lower()

article[add_article] = add_text
print(article)