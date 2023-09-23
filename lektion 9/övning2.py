import  math
pi = math.pi
class Circe():
    def __init__(self, radius):
        self.radius = radius

    def circ_frence(self):
        return (self.radius) * pi

c1 = Circe(10)
print(c1)

