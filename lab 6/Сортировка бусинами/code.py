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
