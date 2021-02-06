from abc import abstractmethod
import math


class BaseFigure:
    def __init__(self):
        self.name = 'base figure',
        self.area = None
        self.perimeter = None,
        self.angles = None

    @abstractmethod
    def add_area(self, add_figure):
        return NotImplemented


class Triangle(BaseFigure):
    def __init__(self, *triangle_sides):
        if len(triangle_sides) != 3:
            print("Input 3 lengths of the sides of the triangle")
        else:
            """Class constructor"""
            super().__init__()
            self.a = triangle_sides[0]
            self.b = triangle_sides[1]
            self.c = triangle_sides[2]

            if self.check_triangle():
                self.angles = 3
                self.name = 'Triangle'
                self.perimeter = self.calculate_perimeter
                self.area = self.calculate_area
            else:
                print("It's not triangle")

    def check_triangle(self):
        return (self.a < self.b + self.c) and (self.b < self.a + self.c) and (self.c < self.a + self.b)

    @property
    def calculate_perimeter(self):
        return round(self.a + self.b + self.c, 2)

    @property
    def calculate_area(self):
        p = self.perimeter / 2
        return round(math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)

    def add_area(self, add_figure):
        if isinstance(add_figure, BaseFigure): return self.area + add_figure.area
        else: return "Entered wrong class"


class Rectangle(BaseFigure):
    def __init__(self, *rectangle_sides):
        if len(rectangle_sides) != 2:
            print("Input 2 lengths of the sides of the rectangle")
        else:
            """Class constructor"""
            super().__init__()
            self.a = rectangle_sides[0]
            self.b = rectangle_sides[1]
            self.angles = 4
            self.name = 'Rectangle'
            self.perimeter = self.calculate_perimeter
            self.area = self.calculate_area

    @property
    def calculate_perimeter(self):
        return round(2 * (self.a + self.b), 2)

    @property
    def calculate_area(self):
        return round((self.a * self.b), 2)

    def add_area(self, add_figure):
        if isinstance(add_figure, BaseFigure): return self.area + add_figure.area
        else: return "Entered wrong class"


class Square(BaseFigure):
    def __init__(self, square_side):
        """Class constructor"""
        super().__init__()
        self.a = square_side
        self.angles = 4
        self.name = 'Square'
        self.perimeter = self.calculate_perimeter
        self.area = self.calculate_area

    @property
    def calculate_perimeter(self):
        return round(4 * self.a, 2)

    @property
    def calculate_area(self):
        return round((self.a * self.a), 2)

    def add_area(self, add_figure):
        if isinstance(add_figure, BaseFigure): return self.area + add_figure.area
        else: return "Entered wrong class"


class Circle(BaseFigure):
    def __init__(self, radius):
        """Class constructor"""
        super().__init__()
        self.r = radius
        self.name = 'Circle'
        self.perimeter = self.calculate_perimeter
        self.area = self.calculate_area

    @property
    def calculate_perimeter(self):
        return round(2 * math.pi * self.r, 2)

    @property
    def calculate_area(self):
        return round(math.pi * self.r * self.r, 2)

    def add_area(self, add_figure):
        if isinstance(add_figure, BaseFigure): return self.area + add_figure.area
        else: return "Entered wrong class"
