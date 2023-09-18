import random
numbers = []

def random_numbergen():
    for x in range (10):
        numbers . append ( random . randint (0 ,20))
    return numbers

def sorted_numbergen():
    return sorted(numbers)

random_number = random_numbergen() 
    
print("\n Before sorting",random_number,)
sorted_number = sorted_numbergen()
print("\n After sorting",sorted_number, "\n") 
