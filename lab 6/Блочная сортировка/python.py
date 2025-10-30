def bucket_sort(arr):
    """
    Блочная сортировка (bucket sort)
    Эффективна для равномерно распределенных данных
    Временная сложность:
      - В лучшем случае: O(n + k)
      - В среднем случае: O(n + k)
      - В худшем случае: O(n²)
    """
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
