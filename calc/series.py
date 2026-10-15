MAX_ITERATIONS = 100000

def term_third(n: int) -> float:
    return ((-1) ** n) / (3 ** n)

def term_sqplus(n: int) -> float:
    return ((-1) ** (n - 1)) / (n ** 2)

def sum_by_terms(term_func, count: int) -> float:
    total_sum = 0.0
    for n in range(1, count + 1):
        if term_func == term_third:
            total_sum += term_func(n - 1)
        else:
            total_sum += term_func(n)
    return total_sum

def sum_by_eps(term_func, eps: float) -> tuple[int, float]:
    total_sum = 0.0
    count = 0
    for i in range(1, MAX_ITERATIONS + 1):
        n = (i - 1) if term_func == term_third else i
        term = term_func(n)
        if abs(term) <= eps:
            break
        total_sum += term
        count += 1
    else:
        raise ValueError("точность не достигнута за максимальное число итераций")
    return count, total_sum

def sum_third(terms: int = None, eps: float = None):
    formula = "1 - 1/3 + 1/9 - 1/27 + ..."
    if terms is not None:
        total_sum = sum_by_terms(term_third, terms)
        return formula, terms, total_sum
    if eps is not None:
        count, total_sum = sum_by_eps(term_third, eps)
        return formula, count, total_sum

def sum_sqplus(terms: int = None, eps: float = None):
    formula = "1 - 1/4 + 1/9 - 1/16 + ..."
    if terms is not None:
        total_sum = sum_by_terms(term_sqplus, terms)
        return formula, terms, total_sum
    if eps is not None:
        count, total_sum = sum_by_eps(term_sqplus, eps)
        return formula, count, total_sum
