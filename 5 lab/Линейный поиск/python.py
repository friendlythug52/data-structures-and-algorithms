def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Пример использования
arr = [3, 5, 2, 7, 9, 1, 4]
target = 7
result = linear_search(arr, target)
print(f"Элемент найден на позиции: {result}" if result != -1 else "Элемент не найден")
