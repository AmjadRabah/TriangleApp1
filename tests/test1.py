import pytest
import numpy as np
from main import triangle
from main import is_int
from main import is_valid_triangle
from main import is_pressed_enter

# global variables
equilateral = 'equilateral'
isosceles = 'isosceles'
scalene = 'scalene'
num_are_val = 'Numbers are valid'
num_are_not_val = 'Numbers are not valid , most be int'
triangle_are_valid = 'Triangle are valid'
triangle_are_not_valid = 'Not Triangle'
triangle_are_not_valid_0 = 'triangle are not valid the numbers most be > 0'
user_pressed_enter = 'user pressed enter'
user_not_pressed_enter = 'user is not pressed enter'
null_numbers = 'null'




def test_check_what_is_the_shape_of_the_triangle():
    """"
    Test that checks triangle function by given numbers in range (0 to 10)
    to check what is the shape of the triangle by different values from the range 
    """""
    for i in range(10):
        for j in range(10):
            for x in range(10):
                if i == j == x:
                    assert triangle(i, j, x) == equilateral
                elif i == j or i == x or j == x:
                    assert triangle(i, j, x) == isosceles
                else:
                    assert triangle(i, j, x) == scalene


@pytest.mark.parametrize("test_input1,test_input2,test_input3,expected", [(1, 0, 1, triangle_are_not_valid_0), (0, 1, 1, triangle_are_not_valid_0), (1, 1, 0, triangle_are_not_valid_0)])
def test_one_sides_are_zero(test_input1, test_input2, test_input3, expected):
    assert is_valid_triangle(test_input1, test_input2, test_input3) == expected


@pytest.mark.parametrize("test_input1,test_input2,test_input3,expected", [(0, 0, 1, triangle_are_not_valid_0), (1, 0, 0, triangle_are_not_valid_0), (0, 1, 0, triangle_are_not_valid_0)])
def test_two_sides_are_zero(test_input1, test_input2, test_input3, expected):
    assert is_valid_triangle(test_input1, test_input2, test_input3) == expected


def test_three_sides_are_zero():
    assert is_valid_triangle(0, 0, 0) == triangle_are_not_valid_0


def test_check_if_all_sides_are_valid_int():
    for i in range(10):
        for j in range(10):
            for x in range(10):
                assert is_int(i, j, x) == num_are_val


@pytest.mark.parametrize("test_input1,test_input2,test_input3,expected", [(0.5, 3.5, 1, num_are_not_val), (1, 0.5, 3.5, num_are_not_val), (0.5, 1, 3.5, num_are_not_val)])
def test_check_if_one_sides_are_valid_int(test_input1, test_input2, test_input3, expected):
    assert is_int(test_input1, test_input2, test_input3) == expected


@pytest.mark.parametrize("test_input1,test_input2,test_input3,expected", [(0.5, 1, 1, num_are_not_val), (1, 0.5, 1, num_are_not_val), (1, 1, 0.5, num_are_not_val)])
def test_check_if_two_sides_are_valid_int(test_input1, test_input2, test_input3, expected):
    assert is_int(test_input1, test_input2, test_input3) == expected


def test_check_if_three_sides_are_not_valid_int():
    for i in np.arange(0.9):
        for j in np.arange(0.9):
            for x in np.arange(0.9):
                assert is_int(i, j, x) == num_are_not_val


@pytest.mark.parametrize("test_input1,test_input2,test_input3,expected", [(0.5, 0.5, 'a', num_are_not_val), ('a', 0.5, 0.5, num_are_not_val), (0.5, 'a', 0.5, num_are_not_val)])
def test_check_if_one_sides_are_char_not_valid_int(test_input1, test_input2, test_input3, expected):
    assert is_int(test_input1, test_input2, test_input3) == expected


@pytest.mark.parametrize("test_input1,test_input2,test_input3,expected", [(0.5, 'b', 'a', num_are_not_val), ('a', 'b', 0.5, num_are_not_val), ('a', 0.5, 'b', num_are_not_val)])
def test_check_if_two_sides_are_char_not_valid_int(test_input1, test_input2, test_input3, expected):
    assert is_int(test_input1, test_input2, test_input3) == expected


def test_check_if_three_sides_are_char_not_valid_int():
    assert is_int('a', 'b', 'c') == num_are_not_val


def test_check_if_three_sides_are_special_characters_not_valid_int():
    assert is_int('!', '@', '%') == num_are_not_val


@pytest.mark.parametrize("test_input1,test_input2,test_input3,expected", [(1, 2, 1, triangle_are_valid), (2, 1, 1, triangle_are_valid), (1, 1, 2, triangle_are_valid)])
def test_check_if_triangle_possible(test_input1, test_input2, test_input3, expected):
    assert is_valid_triangle(test_input1, test_input2, test_input3) == expected


@pytest.mark.parametrize("test_input1,test_input2,test_input3,expected", [(13, 2, 1, triangle_are_not_valid), (2, 1, 13, triangle_are_not_valid), (1, 13, 2, triangle_are_not_valid)])
def test_check_if_triangle_sum_two_side_smaller_than_max(test_input1, test_input2, test_input3, expected):
    assert is_valid_triangle(test_input1, test_input2, test_input3) == expected


def test_user_press_enter():
    assert is_pressed_enter('enter') == user_pressed_enter


def test_user_press_ctrl():
    assert is_pressed_enter('ctrl') == user_not_pressed_enter


def test_three_null():
    assert is_valid_triangle(None, None, None) == null_numbers
    assert is_int(None, None, None) == null_numbers


@pytest.mark.parametrize("test_input1,test_input2,test_input3,expected", [(1, None, None, null_numbers), (None, 1, None, null_numbers), (None, None, 1, null_numbers)])
def test_two_null(test_input1, test_input2, test_input3, expected):
    assert is_valid_triangle(test_input1, test_input2, test_input3) == expected
    assert is_int(test_input1, test_input2, test_input3) == expected


@pytest.mark.parametrize("test_input1,test_input2,test_input3,expected", [(1, 2, None, null_numbers), (None, 1, 2, null_numbers), (2, None, 1, null_numbers)])
def test_one_null(test_input1, test_input2, test_input3, expected):
    assert is_valid_triangle(test_input1, test_input2, test_input3) == expected
    assert is_int(test_input1, test_input2, test_input3) == expected


def test_negative_three_sides_values():
    for i in range(-10):
        for j in range(-10):
            for x in range(-10):
                assert is_valid_triangle(i, j, x) == triangle_are_not_valid_0


@pytest.mark.parametrize("test_input1,test_input2,test_input3,expected", [(-1, -2, 3, triangle_are_not_valid_0), (3, -1, -2, triangle_are_not_valid_0), (-2, 3, -1, triangle_are_not_valid_0)])
def test_negative_two_sides_values(test_input1, test_input2, test_input3, expected):
    assert is_valid_triangle(test_input1, test_input2, test_input3) == expected


@pytest.mark.parametrize("test_input1,test_input2,test_input3,expected", [(-1, 2, 3, triangle_are_not_valid_0), (3, -1, 2, triangle_are_not_valid_0), (2, 3, -1, triangle_are_not_valid_0)])
def test_negative_one_sides_values(test_input1, test_input2, test_input3, expected):
    assert is_valid_triangle(test_input1, test_input2, test_input3) == expected
