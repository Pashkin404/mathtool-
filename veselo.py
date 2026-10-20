

def sel(ar):
    n = len(ar)
    for i in range(n):
        min = i
        for j in range(i+1 , n):
            if ar[j] < ar[min]:
                min = j
        ar[i],ar[i+1] = ar[i+1], ar[i]

def insertion(arr):
    for i in range(1, len(arr)): # Начинаем строго с 1!
        key = arr[i] # Запомнили текущий элемент
        j = i - 1
        while j >= 0 and arr[j] > key: # Пока левый элемент больше, чем key
            arr[j + 1] = arr[j] # Сдвигаем его вправо
            j -= 1
        arr[j + 1] = key # Вставляем наш элемент на освободившееся место
    return arr
print(insertion([2,4,658,2,51,]))

def ins(ar):
    for i in range(1,len(ar)):
        key = ar[i]
        j = i - 1
        while j >= 0 and ar[j]>key:
            ar[j+1] = ar[j]
            j-=1
        ar[j+1] = key
    return ar
print(ins([2,4,658,2,51,]))

