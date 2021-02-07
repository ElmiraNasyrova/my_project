import pytest
import math
from homeworks.dz_6.base_page import Triangle, Rectangle, Circle, Square

R = 18


def test_get_name():
    circle = Circle(R)
    assert circle.get_name().lower() == 'circle'


def test_get_angels():
    circle = Circle(R)
    assert circle.get_angles() == None


def test_get_perimeter():
    circle = Circle(R)
    assert circle.get_perimeter() == round(2 * math.pi * R, 2)


def test_get_area():
    circle = Circle(R)
    assert circle.get_area() == round(math.pi * R * R, 2)


@pytest.mark.parametrize("figure",(Rectangle(5, 7), Triangle(9, 10, 5), Square(10)) )
def test_add_area(figure):
    circle = Circle(R)
    assert circle.add_area(figure) == circle.get_area() + figure.get_area()
