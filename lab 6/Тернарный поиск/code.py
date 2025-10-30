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
