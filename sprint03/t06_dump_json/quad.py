import math
import json


def get_equation(a, b, c):
    equation = str()

    if a != 0:
        if a not in [1, -1]:
            equation += str(a)
        equation += "x^2"

    if b != 0:
        if b < 0:
            equation += "-"
        else:
            equation += "+"
        if b not in [1, -1]:
            equation += str(abs(b))
        equation += "x"

    if c != 0:
        if c > 0:
            equation += "+"
        else:
            equation += "-"
        equation += str(abs(c))
    return equation + "=0"


def get_discriminant(a, b, disc):
    if disc < 0:
        return None
    x1 = round(float((-b - math.sqrt(disc)) / (2 * a)), 3)
    x2 = round(float((-b + math.sqrt(disc)) / (2 * a)), 3)
    x1 = x1 if x1 != -0.0 else 0.0
    x2 = x2 if x2 != -0.0 else 0.0
    if disc == 0:
        return x1
    else:
        return sorted([x1, x2])


def quad(a, b, c):
    result = dict()
    if (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))) and a != 0:
        result["equation"] = get_equation(a, b, c)
        d = b**2 - 4 * a * c
        discriminant = dict({"discriminant": round(float(d), 3), "x": get_discriminant(a, b, d)})
        result["solution"] = discriminant
        return json.dumps(result, indent=3)
    else:
        return 'Cannot generate a quadratic equation.'
