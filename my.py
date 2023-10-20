class Rectangle:
    def __init__(self,a,b):
        self.a = a
       	self.b = b
    def get_area(self):
        return self.a * self.b
class Square:
    def __init__(self,a):
	    self.a = a
    def get_area_square(self):
        return self.a ** 2
class Circle:
    def __init__(self, a):
        self.a = a
    def get_circle(self):
        return (self.a**2)*3.14





# class Dot:
#     def __init__(self,x,y):
#        self.x=x
#        self.y=y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __str__(self):
#         return f'Dot: {self.x, self.y}'
#
# p1 = Dot(1, 2)
# p2 = Dot(1, 2)
# print(p1 == p2)
# print(str(p1))
# print(p2)