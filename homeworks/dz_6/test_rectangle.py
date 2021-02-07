import pytest
from homeworks.dz_6.base_page import Triangle, Rectangle, Circle, Square

A, B = 10, 8


def test_get_name():
    rectangle = Rectangle(A, B)
    assert rectangle.get_name().lower() == 'rectangle'


def test_get_angels():
    rectangle = Rectangle(A, B)
    assert rectangle.get_angles() == 4


def test_get_perimeter():
    rectangle = Rectangle(A, B)
    assert rectangle.get_perimeter() == 2 * (A + B)


def test_get_area():
    rectangle = Rectangle(A, B)
    assert rectangle.get_area() == round(A * B, 2)


@pytest.mark.parametrize("figure", (Triangle(5, 7, 4), Circle(9), Square(10)))
def test_add_area(figure):
    rectangle = Rectangle(A, B)
    assert rectangle.add_area(figure) == rectangle.get_area() + figure.get_area()
