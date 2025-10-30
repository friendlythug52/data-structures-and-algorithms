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
