import pytest
from homeworks.dz_6.base_page import Triangle, Rectangle, Circle, Square

A = 13


def test_get_name():
    square = Square(A)
    assert square.get_name().lower() == 'square'


def test_get_angels():
    square = Square(A)
    assert square.get_angles() == 4


def test_get_perimeter():
    square = Square(A)
    assert square.get_perimeter() == 4 * A


def test_get_area():
    square = Square(A)
    assert square.get_area() == A * A


@pytest.mark.parametrize("figure",(Rectangle(5, 7), Circle(9), Triangle(10, 6, 8)) )
def test_add_area(figure):
    square = Square(A)
    assert square.add_area(figure) == square.get_area() + figure.get_area()
