import shape_calculator

rect = shape_calculator.Rectangle(51, 5)
print('AREA')
print(rect.get_area())
rect.set_height(4)
print('PERIMETRO')
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
print(rect.width)

sq = shape_calculator.Square(2)
print(sq)
sq.set_width(4)
print(sq)