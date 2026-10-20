from calc.arrays import MIN_VALUE, MAX_VALUE

def не_по_порядку(a, b, descending):
    return a < b if descending else a > b

def bubble(массив, descending=False):
    n = len(массив)
    for i in range(n - 1):
        были_обмены = False
        for j in range(n - 1 - i):
            if не_по_порядку(массив[j], массив[j + 1], descending):
                массив[j], массив[j + 1] = массив[j + 1], массив[j]
                были_обмены = True
        if not были_обмены:
            break

METHODS = {
    "bubble": bubble
}
