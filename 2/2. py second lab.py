# Создание мультисписка
multi_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Мультисписок:")
for row in multi_list:
    print(row)

# Добавление нового подсписка
multi_list.append([10, 11, 12])
print("\nПосле добавления:")
for row in multi_list:
    print(row)

# Обращение к элементам
print(f"\nЭлемент [1][2]: {multi_list[1][2]}")  # 6
print(f"Элемент [0][0]: {multi_list[0][0]}")  # 1

# Изменение элемента
multi_list[2][1] = 88
print(f"\nПосле изменения [2][1]: {multi_list[2]}")

# Создание мультисписка разной длины
jagged_list = [
    [1, 2],
    [3, 4, 5, 6],
    [7],
    [8, 9, 10]
]

print("\nЗубчатый мультисписок:")
for row in jagged_list:
    print(row)
