MAX_ITERATIONS = 100000

def sum_third(terms: int = None, eps: float = None):
    total_sum = 0.0
    count = 0
    
    if terms is not None:
        for n in range(terms):
            term = ((-1) ** n) / (3 ** n)
            total_sum += term
        return "1 - 1/3 + 1/9 - 1/27 + ...", terms, total_sum

    if eps is not None:
        for n in range(MAX_ITERATIONS):
            term = ((-1) ** n) / (3 ** n)
            if abs(term) <= eps:
                break
            total_sum += term
            count += 1
        else:
            raise ValueError("требуемая точность не достигнута за максимальное число итераций")
        return "1 - 1/3 + 1/9 - 1/27 + ...", count, total_sum

def sum_sqplus(terms: int = None, eps: float = None):
    total_sum = 0.0
    count = 0
    
    if terms is not None:
        for n in range(1, terms + 1):
            term = ((-1) ** (n - 1)) / (n ** 2)
            total_sum += term
        return "1 - 1/4 + 1/9 - 1/16 + ...", terms, total_sum

    if eps is not None:
        for n in range(1, MAX_ITERATIONS + 1):
            term = ((-1) ** (n - 1)) / (n ** 2)
            if abs(term) <= eps:
                break
            total_sum += term
            count += 1
        else:
            raise ValueError("требуемая точность не достигнута за максимальное число итераций")
        return "1 - 1/4 + 1/9 - 1/16 + ...", count, total_sum
