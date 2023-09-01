choice_number = int(input("Give a number " ))
choice_number_2 = int(input("Give another number " ))
choice_number_3 = int(input("Give another number " ))

if choice_number > choice_number_2 and choice_number > choice_number_3:
    print("The first no. is the biggest number")

elif choice_number_2 > choice_number and choice_number_2 > choice_number_3:
    print(" The second no is the biggest number")

elif choice_number_3 > choice_number and choice_number_3 >choice_number_2:
    print("The third no is the biggest")
