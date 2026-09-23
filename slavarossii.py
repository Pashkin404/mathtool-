import sys
import math

MAX_VALUE = 10000

def print_help():
    print("решение уравнений вида A*x^2 + B*x + C = 0")
    print()
    print("Использование:")
    print("    python mathtool.py                         вывод справки")
    print("    python mathtool.py --help                  вывод справки")
    print("    python mathtool.py solve                   ввод коэффициентов с клавиатуры")
    print("    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами")
    print()
    print("Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.")

def error(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)

def parse_args():
    args = sys.argv[1:]  # отбрасываем имя файла

    if len(args) == 0 or args[0] == "--help":
        print_help()
        sys.exit(0)

    if args[0] != "solve":
        error("ОШИБКА: неизвестная команда")

    if len(args) == 1:
        # ввод коэффициентов с клавиатуры
        return None  # сигнализируем, что нужен интерактивный ввод

    if len(args) == 7:
        if args[1] != "-a" or args[3] != "-b" or args[5] != "-c":
            error("ОШИБКА: неизвестный параметр")
        return args[2], args[4], args[6]  # возвращаем строки, преобразование — далее

    error("ОШИБКА: неверный набор параметров")

def get_coefficients(source):
    """source — кортеж строк (из параметров) или None (интерактивный ввод)."""
    try:
        if source is None:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        else:
            a = int(source[0])
            b = int(source[1])
            c = int(source[2])
    except ValueError:
        error("ОШИБКА: коэффициент не является целым числом")
    return a, b, c

def validate(a, b, c):
    if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
        error("ОШИБКА: значение вне допустимого диапазона")


def solve(a, b, c):
    if a == 0:
        # уравнение не квадратное
        if b != 0:
            print("Уравнение линейное")
            x = -c / b
            print(f"x = {x:.3f}")
        else:
            error("ОШИБКА: это не уравнение, неизвестное отсутствует")
    else:
        # квадратное уравнение
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
