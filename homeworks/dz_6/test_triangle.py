import pytest
import math
from homeworks.dz_6.base_page import Triangle, Rectangle, Circle, Square

A, B, C = 10, 9, 8


def test_get_name():
    triangle = Triangle(A, B, C)
    assert triangle.get_name().lower() == 'triangle'


def test_get_angels():
    triangle = Triangle(A, B, C)
    assert triangle.get_angles() == 3


def test_get_perimeter():
    triangle = Triangle(A, B, C)
    assert triangle.get_perimeter() == A + B +C


def test_get_area():
    triangle = Triangle(A, B, C)

    p = (A + B +C) / 2
    expected_area = round(math.sqrt(p * (p - A) * (p - B) * (p - C)), 2)

    assert triangle.get_area() == expected_area


@pytest.mark.parametrize("figure",(Rectangle(5, 7), Circle(9), Square(10)) )
def test_add_area(figure):
    triangle = Triangle(A, B, C)
    assert triangle.add_area(figure) == triangle.get_area() + figure.get_area()
