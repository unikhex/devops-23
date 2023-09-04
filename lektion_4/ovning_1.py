tal = input("Ange ett heltal:")
try:
tal = int(tal)
kvadrat = tal * tal
print(tal,
"i kvadrat är"
, kvadrat)
except ValueError:
print(tal ,
"är inte ett heltal")