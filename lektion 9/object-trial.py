"""
class Rectangle:
    def __int__(self, length, width):
        """
"""
        Makes them private. And only available in the class
        :param length:
        :param width:
        :return:
        
        self.__width = width
        self.__length = length

     def get_length(self):
         return self.__length
    def get_width(self):
        return  self.__width


    def area(self):
        return self.width * self.length

    def omkrets(self):
        return self.width * 2 + self.length * 2


r1 = Rectangle(20, 30)

print("Width", r1.get_width())
print("Length", r1.get_length())
print("area", r1.area())
print("Omkrets", r1.omkrets()) 
 """

