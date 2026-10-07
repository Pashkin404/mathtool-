import math

def f_ratio(x: float) -> float:
    if x == -1:
        raise ValueError("деление на ноль в функции ratio")
    return x / (x + 1)

def f_root(x: float) -> float:
    return math.sqrt(x ** 2 + 1)

def integrate(func_name: str, start: float, to: float, steps: int):
    if func_name == "ratio":
        if start < 0 or to > 20:
            raise ValueError("для функции ratio пределы интегрирования должны быть внутри [0; 20]")
        f = f_ratio
    elif func_name == "root":
        if start <= -5 or to >= 5:
            raise ValueError("для функции root пределы интегрирования должны быть строго внутри (-5; 5)")
        f = f_root
    else:
        raise ValueError(f"неизвестная функция: '{func_name}'")

    if start >= to:
        raise ValueError("нижний предел должен быть меньше верхнего предела")

    dx = (to - start) / steps
    total_area = 0.0

    for i in range(steps):
        x = start + i * dx
        total_area += f(x)

    return "x / (x + 1)" if func_name == "ratio" else "sqrt(x^2 + 1)", total_area * dx
