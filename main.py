from my import Rectangle, Square, Circle

#далее создаём два прямоугольника

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
#вывод площади наших двух прямоугольников
# print(rect_1.get_area())
# print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

circ_1 = Circle(5)
circ_2 = Circle(5)

# print(square_1.get_area_square(),
#       square_2.get_area_square())

figures = [rect_1, rect_2, square_1, square_2, circ_1, circ_2]
for figure in figures:
    if isinstance (figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_circle())


    # else:
    #     print(figure.get_circle())

