import keyboard

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


def triangle(num1, num2, num3):
    """ Determines the shape of the triangle,
        Returns the shape
      """
    if num1 == num2 and num2 == num3:
        res = equilateral
    elif (num1 == num2 and num1 != num3) or (num1 == num3 and num1 != num2) or (num2 == num3 and num1 != num2):
        res = isosceles
    else:
        res = scalene
    return res


def is_int(num1, num2, num3):
    """ Checks if the numbers are int.
        Returns if the value are valid or not
        """
    if num1 is not None and num2 is not None and num3 is not None:

        if isinstance(num1, int) and isinstance(num2, int) and isinstance(num3, int):
            return num_are_val
        else:
            return num_are_not_val
    else:
        return null_numbers



def is_valid_triangle(num1, num2, num3):
    """ Checks if the triangle are valid.
            Returns if the triangle are valid or not
            """
    if num1 is not None and num2 is not None and num3 is not None:
        if num1 > 0 and num2 > 0 and num3 > 0:
            if num1 + num2 >= num3 and num2 + num3 >= num1 and num3 + num1 >= num2:
                return triangle_are_valid
            else:
                return triangle_are_not_valid
        else:
            return triangle_are_not_valid_0
    else:
        return null_numbers



def is_pressed_enter(val):
    """ Checks if the user pressed enter.
            Returns if the user pressed enter or not
            """
    if val == 'enter':
        return user_pressed_enter
    else:
        return user_not_pressed_enter


def press_enter():
    val = keyboard.read_key()
    while(is_pressed_enter(val) == user_not_pressed_enter):
        print("please re enter\n")
        val = keyboard.read_key()


def get_inputs():
    try:
        n1 = int(input("First Number: "))
        if not type(n1) is int:
            raise TypeError("Only integers are allowed")
        n2 = int(input("second Number: "))
        if not type(n2) is int:
            raise TypeError("Only integers are allowed")
        n3 = int(input("third  Number: "))
        if not type(n3) is int:
            raise TypeError("Only integers are allowed")
        return n1, n2, n3
    except:
        print("Something went wrong")
        return get_inputs()


def main():
    flag = False
    while flag == False:
        lest = get_inputs()
        n1 = lest[0]
        n2 = lest[1]
        n3 = lest[2]
        if is_int(n1, n2, n3) == num_are_val:
            if is_valid_triangle(n1, n2, n3) == triangle_are_valid:
                flag = True
            else:
                print('Not triangle , enter new values')
                flag = False
        else:
            print('Not Int , enter new values')
            flag = False
    print("Is triangle Please press enter to know triangle type")
    press_enter()
    print('The triangle type is: ' + triangle(n1, n2, n3))


if __name__ == '__main__':
    main()

