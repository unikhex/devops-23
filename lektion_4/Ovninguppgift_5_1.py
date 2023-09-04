try:
    inp_no = int(input("Give me a number : "))
    dub_no = inp_no * 2
    print(dub_no)
except ValueError:
    print("Invalid input. Please enter a valid number.")