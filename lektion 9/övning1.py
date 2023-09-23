class Person():
    def __init__(self,name, age,address):
        self.name = name
        self.age = age
        self.address = address

        def __str__(self):
            return f"{self.name}({self.age})({self.address})"

p1 = Person("Zion",21,"Stockholm")
print(p1)

