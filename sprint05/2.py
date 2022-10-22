import cmath


def solve_quadric_equation(a, b, c):
    
    try:
        if type(a) == str or type(b) == str or type(c) == str:
            raise ValueError("Could not convert string to float")
        D = b ** 2 - 4 * a * c
        x1 = (-b - cmath.sqrt(D)) / (2 * a)
        x2 = (-b + cmath.sqrt(D)) / (2 * a)
        return f"The solution are x1={x1} and x2={x2}"
    except ZeroDivisionError:
        return "Zero Division Error"
    except ValueError as e:
        return e

print(solve_quadric_equation(1, 4, 5))