country = input("What is your country: ")
l_nord = [
    "Danmark",
    "Finland",
    "Island",
    "Norge",
    "Sverige"
]

l_britain = [
    "England",
    "Nordiland",
    "Skottland",
    "Wales"
]
if country in l_nord:
    print("Du bor i Norden")
elif country in l_britain:
    print("Du bor i Strobritanien")
else:
    print("You aren't living in either Norden or  Storbritanien")
 