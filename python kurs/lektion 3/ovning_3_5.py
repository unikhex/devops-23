sex = input("What is your sex? man or woman :")
hair_colour = input("What is your hairclour :")
eye_colour = input("What is your eye colour :")

u_p = [sex, hair_colour, eye_colour]

daniel_radcliffe = ["man", "brown", "brown"]
rupert_grint = ["man","blue","blue"]
emma_watson = ["woman", "brown", "brown"]
selena_gomez = ["woman", "brown", "brown"]


if u_p == daniel_radcliffe:
    print("You have the same characteristics as daniel radcliffe")
elif u_p == rupert_grint:
    print("You have the same characteristics as rupert grint")
elif u_p == emma_watson:
    print("You have the same characteristics as emma watson and selena gomez")
else:
    print("You dont look like anyone lol")