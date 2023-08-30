"""
a = 5
b = "5"
c = a + b #Värför kraschar programmet?
"""
#The code crashes since the values are of different types which makes the computer confused on what to do with them.
#So by having them in the same data type it will undestand and run the code.
#Lastly there is no command to call back c.
# It should instead look like this

a = 5
b = "5"
c = a + int(b) 
print (c) 