# Блинная сортировка 

def pancake_sort(arr):
    """
    Блинная сортировка (pancake sort)
    Использует только операцию переворота префикса массива
    Временная сложность: O(n²)
    """
    n = len(arr)

    # Проходим от конца массива к началу
    for curr_size in range(n, 1, -1):
        # Находим индекс максимального элемента в неотсортированной части
        max_idx = arr.index(max(arr[:curr_size]))

        # Если максимальный элемент не на своем месте
        if max_idx != curr_size - 1:
            # Переворачиваем до максимального элемента
            if max_idx != 0:
                arr = flip(arr, max_idx)

            # Переворачиваем весь подмассив
            arr = flip(arr, curr_size - 1)

    return arr


def flip(arr, k):
    """Переворачивает префикс массива до индекса k включительно"""
    left = 0
    while left < k:
        arr[left], arr[k] = arr[k], arr[left]
        left += 1
        k -= 1
    return arr

print(pancake_sort([1, 8, 3, 4, 5, 6, 7, 2, 10, 9]))



#Вывод из консоли: 
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

################################################################################################

#Блочная (корзинная) сортировка
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Определяем количество корзин
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Распределяем элементы по корзинам
    max_val = max(arr)
    for num in arr:
        index = min(n - 1, int(num * n / (max_val + 1)))
        buckets[index].append(num)

    # Сортируем каждую корзину и объединяем
    result = []
    for bucket in buckets:
        # Используем сортировку вставками для каждой корзины
        insertion_sort(bucket)
        result.extend(bucket)

    return result


def insertion_sort(arr):
    """Вспомогательная функция: сортировка вставками"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


print(bucket_sort([7, 2, 3, 4, 10, 6, 1, 8, 9, 5]))


################################################################################################

#Поиск скачками

import math


def jump_search(arr, target):
    """
    Поиск скачками (jump search)
    Для отсортированных массивов
    Временная сложность: O(√n)
    """
    n = len(arr)
    if n == 0:
        return -1

    # Определяем размер прыжка
    step = int(math.sqrt(n))

    # Находим блок, где может находиться элемент
    prev = 0
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Линейный поиск в найденном блоке
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1

print(jump_search([1, 2, 3, 4, 5], 4))

#Вывод консоли: 3



#Вывод из консоли: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


################################################################################################

#Сортировка бусинами

def bead_sort(arr):
    """
    Сортировка бусинами (bead sort)
    Работает только для неотрицательных целых чисел
    Временная сложность: 
      - Теоретически: O(n)
      - Практически: O(S), где S - сумма всех элементов
    """
    if not arr:
        return []
    
    # Находим максимальное значение
    max_val = max(arr)
    
    # Создаем "абак" - матрицу бусин
    beads = [[0] * len(arr) for _ in range(max_val)]
    
    # Расставляем бусины (1 - есть бусина, 0 - нет)
    for i, num in enumerate(arr):
        for j in range(num):
            beads[j][i] = 1
    
    # "Падение" бусин под действием гравитации
    for i in range(max_val):
        # Считаем количество бусин в строке
        bead_count = sum(beads[i])
        
        # Перемещаем бусины вниз
        for j in range(len(arr)):
            if j < bead_count:
                beads[i][j] = 1
            else:
                beads[i][j] = 0
    
    # Считываем результат снизу вверх
    result = []
    for j in range(len(arr)):
        count = 0
        for i in range(max_val):
            count += beads[i][j]
        result.append(count)
    
    return result
print(bead_sort([10, 2, 3, 4, 5, 9, 7, 8, 6, 1]))

#Вывод из консоли:[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


################################################################################################

#Тернарный поиск

def ternary_search(arr, target):
    """
    Тернарный поиск (ternary search)
    Делит диапазон на три части
    Временная сложность: O(log₃n)
    """
    return ternary_search_recursive(arr, target, 0, len(arr) - 1)


def ternary_search_recursive(arr, target, left, right):
    """Рекурсивная реализация тернарного поиска"""
    if left > right:
        return -1

    # Делим диапазон на три части
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    # Проверяем граничные точки
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2

    # Определяем, в какой трети продолжать поиск
    if target < arr[mid1]:
        return ternary_search_recursive(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search_recursive(arr, target, mid2 + 1, right)
    else:
        return ternary_search_recursive(arr, target, mid1 + 1, mid2 - 1)

print(ternary_search([1, 2, 3, 4, 5], 5))

#Вывод консоли:4


################################################################################################


#Экспоненциальный поиск 

def exponential_search(arr, target):
    """
    Экспоненциальный поиск (exponential search)
    Для больших отсортированных массивов
    Временная сложность: O(log n)
    """
    n = len(arr)
    if n == 0:
        return -1

    # Если элемент в начале
    if arr[0] == target:
        return 0

    # Экспоненциально увеличиваем диапазон
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    # Бинарный поиск в найденном диапазоне
    return binary_search(arr, target, i // 2, min(i, n - 1))


def binary_search(arr, target, left, right):
    """Вспомогательная функция: бинарный поиск"""
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(exponential_search([1, 2, 3, 4, 5], 5))


#Вывод консоли:4
