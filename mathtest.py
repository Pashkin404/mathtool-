import sys
import math
from cli import setup_parser
from calc.equation import solve
import calc.stats as stats  
import calc.series as series
import calc.integration as integration  

MAX_STATS_VALUE = 10000

def handle_solve(args):
    coefs = [args.a, args.b, args.c]
    count_given = sum(1 for x in coefs if x is not None)
    
    if count_given == 0:
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:
            raise ValueError("коэффициент не является целым числом")
    elif count_given == 3:
        a, b, c = args.a, args.b, args.c
    else:
        raise ValueError("укажите все три коэффициента либо ни одного")

    kind, d, roots = solve(a, b, c)
    if kind == "линейное":
        print("Уравнение линейное")
    else:
        print("Уравнение квадратное")
        
    if d is not None:
        print(f"Дискриминант: {d}")
        
    if len(roots) == 2:
        print(f"x1 = {roots[0]:.3f}")
        print(f"x2 = {roots[1]:.3f}")
    elif len(roots) == 1:
        print(f"x = {roots[0]:.3f}")
    else:
        print("Действительных корней нет")
    return 0

def handle_stats(args):
    if args.input:
        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            raise ValueError(f"файл '{args.input}' не найден")
    else:
        lines = sys.stdin.readlines()

    values = []
    for line in lines:
        for token in line.split():
            try:
                val = float(token)
                if not math.isfinite(val):
                    raise ValueError("обнаружено некорректное число (NaN или Infinity)")
                if abs(val) > MAX_STATS_VALUE:
                    raise ValueError(f"число {val} превышает по модулю {MAX_STATS_VALUE}")
                
                values.append(val)
                if len(values) > 20:
                    raise ValueError("последовательность содержит более 20 чисел")
            except ValueError as e:
                if "превышает" in str(e) or "содержит" in str(e) or "NaN" in str(e):
                    raise e
                raise ValueError(f"некорректный элемент ввода: '{token}'")

    if not values:
        raise ValueError("последовательность пуста")

    metrics = [
        ("Сумма", stats.get_sum, True),
        ("Среднее арифметическое", stats.get_mean, True),
        ("Сумма квадратов элементов", stats.get_sum_sq, True),
        ("Среднее квадратическое", stats.get_rms, True),
        ("Дисперсия", stats.get_variance, True),
        ("СКО (отклонение по N)", stats.get_std_dev_n, True),
        ("Стандартное отклонение (отклонение по N - 1)", stats.get_std_dev_n1, True),
        ("Наименьшее значение", stats.get_min, True),
        ("Наибольшее значение", stats.get_max, True),
        ("Количество положительных чисел", stats.get_positives, False),
        ("Количество отрицательных чисел", stats.get_negatives, False)
    ]

    for label, func, is_float in metrics:
        res = func(values)
        if res is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            if is_float:
                print(f"{label}: {res:.3f}")
            else:
                print(f"{label}: {res}")
    return 0

def handle_series(args):
    series_map = {
        "third": series.sum_third,
        "sqplus": series.sum_sqplus
    }
    
    if args.func not in series_map:
        raise ValueError(f"неизвестное имя ряда: '{args.func}'")
        
    if args.terms is not None and (args.terms < 1 or args.terms > 10000):
        raise ValueError("количество слагаемых должно быть в диапазоне от 1 до 10000")
    if args.eps is not None and (args.eps <= 0 or args.eps > 0.0001):
        raise ValueError("точность должна быть строго больше 0 и не превышать 0.0001")

    calc_func = series_map[args.func]
    formula, count, total_sum = calc_func(terms=args.terms, eps=args.eps)
    
    print(f"Формула ряда: {formula}")
    print(f"Количество слагаемых: {count}")
    print(f"Сумма ряда: {total_sum:.4f}")
    return 0

def handle_integrate(args):
    if args.steps < 1 or args.steps > 100000:
        raise ValueError("количество шагов должно быть в диапазоне от 1 до 100000")

    formula, result_val = integration.integrate(
        func_name=args.func,
        start=args.start,
        to=args.to,
        steps=args.steps
    )

    print(f"Формула функции: {formula}")
    print(f"Значение интеграла: {result_val:.4f}")
    return 0

def main(argv):
    parser = setup_parser()
    args = parser.parse_args(argv)
    
    if args.command is None:
        parser.print_help()
        return 0
        
    try:
        if args.command == "solve":
            return handle_solve(args)
        elif args.command == "stats":
            return handle_stats(args)
        elif args.command == "series":
            return handle_series(args)
        elif args.command == "integrate":
            return handle_integrate(args)
            
    except ValueError as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
