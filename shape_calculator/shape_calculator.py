class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            picture = ''
            for i in range(self.height):
                picture += '*'*self.width + '\n'
        return picture
    def get_amount_inside(self, shape): 
        # shape_area = shape.get_area()
        # class_area = self.get_area()
        # if class_area >= shape_area:
        #     fit = class_area // shape_area
        #     return fit
        # else:
        #     return 0
        return (self.width//shape.width)*(self.height//shape.height)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    
    def __init__(self, side):
        # self.side_length = side
        self.width = self.height = side
    
    def set_side(self, side):
        # self.side_length = side
        self.width = self.height = side 

    def set_width(self, side):
        self.width = self.height = side
        

    def set_height(self, side):
        self.height = self.width = side
          
    def __str__(self):
        return f'Square(side={self.width})'
