import unittest


def quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    
    try:
        if a == 0 and b == 0 and c == 0:
            raise ValueError
    except ValueError:
        print("error")
    else:
        if discriminant > 0:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)   
            return x1, x2
        elif discriminant == 0:
            x = -b / 2 * a
            return x


class QuadraticEquationTest(unittest.TestCase):
    
    def test_discriminant_less_than_zero(self):
        expected = None
        actual = quadratic_equation(4, 5, 3)
        self.assertEqual(actual, expected)

    def test_discriminant_greater_than_zero(self):
        expected = (0.5, -3.0)
        actual = quadratic_equation(2, 5, -3)
        self.assertEqual(actual, expected)

    def test_discriminant_is_equal_to_zero(self):
        expected = 1.0
        actual = quadratic_equation(1, -2, 1)
        self.assertEqual(actual, expected)
    
    def test_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, quadratic_equation, 0, 3, 2)
