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
