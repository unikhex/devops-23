my_bill = float(input("What was the bill?  ")) #writes in decimal
numberOfPeople = int(input("How many people?: "))#writes in whole number
answer = my_bill / numberOfPeople
answer = round(answer) #rounds the answer up or down
print("You all owe �", answer)