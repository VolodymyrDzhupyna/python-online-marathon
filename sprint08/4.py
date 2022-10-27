import unittest
from collections.abc import Iterable


class TriangleNotValidArgumentException(Exception):
    
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class TriangleNotExistException(Exception):
    
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Triangle:
    
    def __init__(self, sides):
        self.sides = sides
        if not isinstance(self.sides, Iterable) or len(self.sides) != 3:
            raise TriangleNotValidArgumentException("Not valid arguments")
        for item in self.sides:
            if isinstance(item, str):
                raise TriangleNotValidArgumentException("Not valid arguments")
        if (((self.sides[0] + self.sides[1]) <= self.sides[2])
            or ((self.sides[0] + self.sides[2]) <= self.sides[1])
            or ((self.sides[1] + self.sides[2]) <= self.sides[0])):
                raise TriangleNotExistException("Can`t create triangle with this arguments")

    def get_area(self):
        a, b, c = self.sides
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area


class TriangleTest(unittest.TestCase):

    def test_valid_data(self):
        valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]
        for item in valid_test_data:
            with self.subTest(item=item):
                self.assertAlmostEqual(Triangle(item[0]).get_area(), item[1], 1)

    def test_not_valid_triangle(self):
        not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]
        for item in not_valid_triangle:
            with self.assertRaises(expected_exception=TriangleNotExistException):
                self.assertRaises(TriangleNotExistException, Triangle(item))
    
    def test_not_valid_arguments(self):
        not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            (7, "str", 7),
            ('1', '1', '1'),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            'str',
            10,
            ('a', 'str', 7)
        ]
        for item in not_valid_arguments:
            with self.assertRaises(expected_exception=TriangleNotValidArgumentException):
                self.assertRaises(TriangleNotValidArgumentException, Triangle(item))

triangle = Triangle([3, 4, 5])
print(triangle.get_area())

not_valid_arguments = [
    ('3', 4, 5),
    ('a', 2, 3),
    'string',
    (7, 2),
    (7, 7, 7, 7),
    10
]

not_valid_triangle = [
    (1, 2, 3),
    (1, 1, 2),
    (7, 7, 15),
    (100, 7, 90),
    (17, 18, 35),
    (127, 17, 33),
    (145, 166, 700),
    (1000, 2000, 1),
    (717, 17, 7),
    (0, 7, 7),
    (-7, 7, 7)
]

for data in not_valid_arguments:
    try:
        Triangle(data)
    except TriangleNotValidArgumentException as e:
        print(e)


for data in not_valid_triangle:
    try:
        Triangle(data)
    except TriangleNotExistException as e:
        print(e)
