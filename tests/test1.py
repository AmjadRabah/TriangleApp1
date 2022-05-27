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


def test_check_if_the_shape_is_isosceles():
    assert triangle(2, 2, 3) == isosceles


def test_check_if_the_shape_is_equilateral():
    assert triangle(1, 1, 1) == equilateral


def test_check_if_the_shape_is_scalene():
    assert triangle(1, 2, 3) == scalene


def test_one_sides_are_zero():
    assert is_valid_triangle(0, 1, 1) == triangle_are_not_valid_0


def test_two_sides_are_zero():
    assert is_valid_triangle(0, 0, 1) == triangle_are_not_valid_0


def test_three_sides_are_zero():
    assert is_valid_triangle(0, 0, 0) == triangle_are_not_valid_0


def test_check_if_all_sides_are_valid_int():
    assert is_int(1, 1, 1) == num_are_val


def test_check_if_one_sides_are_valid_int():
    assert is_int(1, 1.5, 14.5) == num_are_not_val


def test_check_if_two_sides_are_valid_int():
    assert is_int(1, 1, 1.5) == num_are_not_val


def test_check_if_three_sides_are_not_valid_int():
    assert is_int(1.5, 1.5, 1.5) == num_are_not_val


def test_check_if_one_sides_are_char_not_valid_int():
    assert is_int('a', 1.5, 1.5) == num_are_not_val


def test_check_if_two_sides_are_char_not_valid_int():
    assert is_int('a', 'b', 1.5) == num_are_not_val


def test_check_if_three_sides_are_char_not_valid_int():
    assert is_int('a', 'b', 'c') == num_are_not_val


def test_check_if_three_sides_are_special_characters_not_valid_int():
    assert is_int('!', '@', '%') == num_are_not_val


def test_check_if_triangle_possible():
    assert is_valid_triangle(1, 2, 1) == triangle_are_valid


def test_check_if_triangle_sum_two_side_smaller_than_max():
    assert is_valid_triangle(13, 2, 1) == triangle_are_not_valid


def test_user_press_enter():
    assert is_pressed_enter('enter') == user_pressed_enter


def test_user_press_ctrl():
    assert is_pressed_enter('ctrl') == user_not_pressed_enter


def test_three_null():
    assert is_valid_triangle(None, None, None) == null_numbers
    assert is_int(None, None, None) == null_numbers


def test_two_null():
    assert is_valid_triangle(1, None, None) == null_numbers
    assert is_int(1, None, None) == null_numbers


def test_one_null():
    assert is_valid_triangle(1, 2, None) == null_numbers
    assert is_int(1, 2, None) == null_numbers


def test_negative_three_sides_values():
    assert is_valid_triangle(-1, -2, -3) == triangle_are_not_valid_0


def test_negative_two_sides_values():
    assert is_valid_triangle(-1, -2, 3) == triangle_are_not_valid_0


def test_negative_one_sides_values():
    assert is_valid_triangle(-1, 2, 3) == triangle_are_not_valid_0
