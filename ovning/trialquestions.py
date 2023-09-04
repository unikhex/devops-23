"""
a = 5
b = "5"
c = a + b #Värför kraschar programmet?
"""
#The code crashes since the values are of different types which makes the computer confused on what to do with them.
#So by having them in the same data type it will undestand and run the code.
#Lastly there is no command to call back c.
# It should instead look like this
"""
a = 5
b = "5"
c = a + int(b) 
print (c) 
"""

"""
en_mening = " This is a string"
print(en_mening)
"""
"""
Christian =1337
MittNamn = Christian
print ( MittNamn )
# OUTPUT : 1337 
This is not a string. It becomes a variable since there ae no quotes
"""

"""
mening =" alla ord b¨o rjar p˚a stor bokstav "
ny_variabel = mening . title ()
print ( ny_variabel )"""

"""
print (’Vad ¨ar ditt f¨o rnamn ?’)
first_name = input ()
print (’Vad ¨ar ditt efternamn ?’)
last_name = input ()
full_name = first_name + ’ ’ + last_name
print (’Hall ˚a ’ + full_name + ’!’)
"""