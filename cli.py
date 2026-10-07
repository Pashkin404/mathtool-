import argparse

def setup_parser():
    parser = argparse.ArgumentParser(
        prog="mathtest",
        description="mathtest — утилита для математических расчетов и анализа последовательностей.",
        allow_abbrev=False
    )
    
    subparsers = parser.add_subparsers(dest="command")
    
    solve_parser = subparsers.add_parser("solve", help="Решение квадратных и линейных уравнений", allow_abbrev=False)
    solve_parser.add_argument("-a", type=int, help="Коэффициент A")
    solve_parser.add_argument("-b", type=int, help="Коэффициент B")
    solve_parser.add_argument("-c", type=int, help="Коэффициент C")
    
    stats_parser = subparsers.add_parser("stats", help="Вычисление показателей последовательности", allow_abbrev=False)
    stats_parser.add_argument("--input", type=str, help="Имя входного файла (если не задан, читает stdin)")
    
    series_parser = subparsers.add_parser("series", help="Вычисление суммы ряда", allow_abbrev=False)
    series_parser.add_argument("--func", type=str, required=True, help="Имя ряда (sqplus, third)")
    series_group = series_parser.add_mutually_exclusive_group(required=True)
    series_group.add_argument("--terms", type=int, help="Количество слагаемых (1..10000)")
    series_group.add_argument("--eps", type=float, help="Точность вычисления (>0 и <=0.0001)")
    
    integrate_parser = subparsers.add_parser("integrate", help="Численное интегрирование функции", allow_abbrev=False)
    integrate_parser.add_argument("--func", type=str, required=True, help="Имя функции (ratio, root)")
    integrate_parser.add_argument("--from", dest="start", type=float, required=True, help="Нижний предел интегрирования")
    integrate_parser.add_argument("--to", type=float, required=True, help="Верхний предел интегрирования")
    integrate_parser.add_argument("--steps", type=int, required=True, help="Количество шагов сетки (1..100000)")
    
    return parser
