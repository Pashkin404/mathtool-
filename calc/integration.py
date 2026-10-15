import math

RATIO_MIN, RATIO_MAX = 0.0, 20.0
ROOT_MIN, ROOT_MAX = -5.0, 5.0

def f_ratio(x: float) -> float:
    if x == -1:
        raise ValueError("деление на ноль в функции ratio")
    return x / (x + 1)

def f_root(x: float) -> float:
    return math.sqrt(x ** 2 + 1)

FUNCTIONS_TABLE = {
    "ratio": (f_ratio, "x / (x + 1)", RATIO_MIN, RATIO_MAX, False),
    "root":  (f_root,  "sqrt(x^2 + 1)", ROOT_MIN,  ROOT_MAX,  True)
}

def integrate(func_name: str, start: float, to: float, steps: int):
    if func_name not in FUNCTIONS_TABLE:
        raise ValueError(f"неизвестная функция: '{func_name}'")
        
    func, formula_text, low, high, is_strict = FUNCTIONS_TABLE[func_name]

    if not math.isfinite(start) or not math.isfinite(to):
        raise ValueError("пределы интегрирования должны быть конечными числами")
        
    if start >= to:
        raise ValueError("нижний предел должен быть меньше верхнего предела")

    if is_strict:
        if start <= low or to >= high:
            raise ValueError(f"для функции {func_name} пределы должны быть строго внутри ({low}; {high})")
    else:
        if start < low or to > high:
            raise ValueError(f"для функции {func_name} пределы должны быть внутри [{low}; {high}]")

    dx = (to - start) / steps
    total_area = 0.0

    for i in range(steps):
        x = start + i * dx
        total_area += func(x)

    return formula_text, total_area * dx
