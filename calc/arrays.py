import random

MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1_000_000
MAX_SEARCH = 1000

def заполнить(count, low=MIN_VALUE, high=MAX_VALUE, seed=None):
    if seed is not None:
        random.seed(seed)
    return [random.randint(low, high) for _ in range(count)]

def двоичный_поиск(массив, искомое):
    левая, правая = 0, len(массив) - 1
    while левая <= правая:
        середина = (левая + правая) // 2
        if массив[середина] == искомое:
            return середина
        elif массив[середина] < искомое:
            левая = середина + 1
        else:
            правая = середина - 1
    return None
