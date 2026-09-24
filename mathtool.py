import sys
import math

MAX_VALUE = 10000

def error(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)

def print_help():
    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0")
    print("Использование:")
    print("    python mathtool.py                         вывод справки")
    print("    python mathtool.py --help                  вывод справки")
    print("    python mathtool.py solve                   ввод коэффициентов с клавиатуры")
    print("    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами\n")
    print(f"Коэффициенты A, B, C — целые числа, по модулю не превышающие {MAX_VALUE}.")

def parse_args():
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] == "--help"):
        print_help()
        sys.exit(0)

    if sys.argv[1] != "solve":
        error("ОШИБКА: неизвестная команда")

    if len(sys.argv) == 2:
        return None

    if len(sys.argv) == 8:
        if sys.argv[2] != "-a" or sys.argv[4] != "-b" or sys.argv[6] != "-c":
            error("ОШИБКА: неизвестный параметр")
        return sys.argv[3], sys.argv[5], sys.argv[7]

    error("ОШИБКА: неверный набор параметров")

def get_coefficients(source):
    try:
        if source is None:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        else:
            a = int(source[0])
            b = int(source[1])
            c = int(source[2])
        return a, b, c
    except ValueError:
        error("ОШИБКА: коэффициент не является целым числом")

def validate(a, b, c):
    if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
        error("ОШИБКА: значение вне допустимого диапазона")

def solve(a, b, c):
    if a == 0:
        if b != 0:
            print("Уравнение линейное")
            x = -c / b
            print(f"x = {x:.3f}")
        else:
            error("ОШИБКА: это не уравнение, неизвестное отсутствует")
    else:
        print("Уравнение квадратное")
        d = b * b - 4 * a * c
        print(f"Дискриминант = {d}")
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print(f"x1 = {x1:.3f}")
            print(f"x2 = {x2:.3f}")
        elif d == 0:
            x = -b / (2 * a)
            print(f"x = {x:.3f}")
        else:
            print("Действительных корней нет")

def main():
    source = parse_args()
    a, b, c = get_coefficients(source)
    validate(a, b, c)
    solve(a, b, c)
    sys.exit(0)

if __name__ == "__main__":
    main()
