"""
name_1 = input("What is yout name: ")
age_1 = int(input("What is your age: "))

if age_1 == 1:
    print("Halå", name_1,". Enligt Vårdguidens rekommendaktioner behöver individer i din ålder",age_1 , "sova minst 14 timmar" )
elif age_1 == 2:
    print("Halå", name_1,". Enligt Vårdguidens rekommendaktioner behöver individer i din ålder",age_1, "sova minst 13 timmar" )
elif age_1 == 3:
    print("Halå", name_1,". Enligt Vårdguidens rekommendaktioner behöver individer i din ålder",age_1, "sova minst 12 timmar" )
elif age_1 == 4:
    print("Halå", name_1,". Enligt Vårdguidens rekommendaktioner behöver individer i din ålder",age_1, "sova minst 11,5 timmar" )
elif age_1 == 5 and age_1 == 6:
    print("Halå", name_1,". Enligt Vårdguidens rekommendaktioner behöver individer i din ålder",age_1, "sova minst 11 timmar" )
elif age_1 == 7:
    print("Halå", name_1,". Enligt Vårdguidens rekommendaktioner behöver individer i din ålder",age_1, "sova minst 10,5 timmar" )
elif age_1 == 8 and age_1 == 9 and age_1 == 10:
    print("Halå", name_1,". Enligt Vårdguidens rekommendaktioner behöver individer i din ålder",age_1, "sova minst 10 timmar" )
elif age_1 == 11:
    print("Halå", name_1,". Enligt Vårdguidens rekommendaktioner behöver individer i din ålder",age_1, "sova minst 9,5 timmar" )
elif age_1 >= 12 or age_1 <= 15:
    print("Halå", name_1,". Enligt Vårdguidens rekommendaktioner behöver individer i din ålder",age_1, "sova minst 9 timmar" )
elif age_1 == 16:
    print("Halå", name_1,". Enligt Vårdguidens rekommendaktioner behöver individer i din ålder",age_1, "sova minst 8,5 timmar" )
else:
    print("Halå", name_1,". Enligt Vårdguidens rekommendaktioner behöver individer i din ålder",age_1, "sova minst 8 timmar" )"""

name = input("What is your name: ")
age = int(input("What is your age: "))

# Define a dictionary to map ages to recommended sleep hours
age_to_sleep_hours = {
    1: 14,
    2: 13,
    3: 12,
    4: 11.5,
    5: 11,
    6: 11,
    7: 10.5,
    8: 10,
    9: 10,
    10: 10,
    11: 9.5,
}

# Default sleep hours for ages not in the dictionary
default_sleep_hours = 8

# Get the recommended sleep hours based on age or use the default
recommended_sleep_hours = age_to_sleep_hours.get(age, default_sleep_hours)

# Print the message
print(f"Hello {name}. According to Vårdguiden's recommendations, individuals your age should sleep at least {recommended_sleep_hours} hours.")
