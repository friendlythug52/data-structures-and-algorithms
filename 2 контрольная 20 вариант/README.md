***Задание 20. Имитация отжига для задачи размещения центров***
Условие. Разместить k центров на плоскости так, чтобы минимизировать суммарное 
расстояние от каждой из n точек‑клиентов до ближайшего центра.
Алгоритм: имитация отжига: случайное смещение центров, принятие решения по критерию 
Метрополиса.
Язык примера: C++
vector<pair<double, double>> sa_facility_location(
 const vector<pair<double, double>>& clients,
 int k, double temp, double cooling
) {
 // Инициализация: случайные позиции k центров
 vector<pair<double, double>> centers(k);
 for (int i = 0; i < k; i++) {
 centers[i] = {
 random_double(-10, 10),
 random_double(-10, 10)
 };
 }
 double current_cost = totalDistance(clients, centers);
 while (temp > 1e-6) {
 // Создаём кандидата: сдвигаем один случайный центр
 vector<pair<double, double>> new_centers = centers;
 int idx = random_int(0, k - 1);
 new_centers[idx].first += random_double(-1, 1) * temp;
 new_centers[idx].second += random_double(-1, 1) * temp;
 double new_cost = totalDistance(clients, new_centers);
 // ДОПИСАТЬ: принять/отклонить new_centers по критерию Метрополиса
 // Если принято, обновить centers и current_cost
 temp *= cooling;
 }
 return centers;
}
Что дописать:
1. Условие принятия нового решения:
o если new_cost < current_cost, принимаем;
o иначе принимаем с вероятностью exp((current_cost - new_cost)/temp).
2. Обновление centers и current_cost при принятии.
Примечания:
• Функция totalDistance считает сумму расстояний от каждого клиента до 
ближайшего центра.
• random_double(a, b) возвращает случайное число из [a,b].
• random_int(a, b) возвращает случайное целое из [a,b]
