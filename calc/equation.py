import math

MAX_VALUE = 10000

def validate_coefficients(coefficients: dict):
    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"коэффициент {name} вне допустимого диапазона")

def solve(a: int, b: int, c: int):
    validate_coefficients({"A": a, "B": b, "C": c})
    
    if a == 0:
        if b == 0:
            raise ValueError("это не уравнение")
        return "линейное", None, [-c / b]
    
    d = b * b - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return "квадратное", d, [x1, x2]
    elif d == 0:
        x = -b / (2 * a)
        return "квадратное", d, [x]
    else:
        return "квадратное", d, []
