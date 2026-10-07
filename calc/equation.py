# calc/equation.py
import math

# Константа предела из задания
MAX_VALUE = 10000

def validate_coefficients(coefficients: dict):
    """Проверяет коэффициенты на выход за границы диапазона через словарь.
    
    Если значение не валидно, возбуждает ValueError (без print!).
    """
    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"коэффициент {name} вне допустимого диапазона")

def solve(a: int, b: int, c: int):
    """Вычисляет корни квадратного или линейного уравнения.
    
    Не выполняет ввод-вывод. Возвращает вид уравнения, дискриминант и список корней.
    """
    # Оптимизированная проверка без дублирования кода
    validate_coefficients({"A": a, "B": b, "C": c})
    
    # Случай линейного уравнения
    if a == 0:
        if b == 0:
            raise ValueError("это не уравнение")
        # Передаем: тип, отсутствие дискриминанта (None), список с одним корнем
        return "линейное", None, [-c / b]
    
    # Случай квадратного уравнения
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
