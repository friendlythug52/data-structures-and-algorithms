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
