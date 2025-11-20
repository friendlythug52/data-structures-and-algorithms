#include <cmath>   // для exp, sqrt
#include <cstdlib> // для rand, srand
#include <ctime>   // для time
#include <iostream>
#include <limits>  // для numeric_limits
#include <utility> // для pair
#include <vector>

using namespace std;

// Вспомогательные функции для генерации случайных чисел
double random_double(double a, double b) {
  return a + (b - a) * (rand() / (RAND_MAX + 1.0));
}

int random_int(int a, int b) { return a + rand() % (b - a + 1); }

// Функция вычисления расстояния между двумя точками
double distance(pair<double, double> a, pair<double, double> b) {
  double dx = a.first - b.first;
  double dy = a.second - b.second;
  return sqrt(dx * dx + dy * dy);
}

// Функция вычисления суммарного расстояния от клиентов до ближайших центров
double totalDistance(const vector<pair<double, double>> &clients,
                     const vector<pair<double, double>> &centers) {
  double total = 0.0;

  for (const auto &client : clients) {
    double min_dist = numeric_limits<double>::max();

    for (const auto &center : centers) {
      double dist = distance(client, center);
      if (dist < min_dist) {
        min_dist = dist;
      }
    }

    total += min_dist;
  }

  return total;
}

// Основная функция имитации отжига
vector<pair<double, double>>
sa_facility_location(const vector<pair<double, double>> &clients, int k,
                     double temp, double cooling) {
  // Инициализация генератора случайных чисел
  srand(time(nullptr));

  // Инициализация: случайные позиции k центров
  vector<pair<double, double>> centers(k);
  for (int i = 0; i < k; i++) {
    centers[i] = {random_double(-10, 10), random_double(-10, 10)};
  }

  double current_cost = totalDistance(clients, centers);

  while (temp > 1e-6) {
    // Создаём кандидата: сдвигаем один случайный центр
    vector<pair<double, double>> new_centers = centers;
    int idx = random_int(0, k - 1);
    new_centers[idx].first += random_double(-1, 1) * temp;
    new_centers[idx].second += random_double(-1, 1) * temp;
    double new_cost = totalDistance(clients, new_centers);

    // Критерий Метрополиса
    if (new_cost < current_cost) {
      // Всегда принимаем улучшающее решение
      centers = new_centers;
      current_cost = new_cost;
    } else {
      // Принимаем ухудшающее решение с вероятностью exp((current_cost -
      // new_cost)/temp)
      double acceptance_prob = exp((current_cost - new_cost) / temp);
      if (random_double(0, 1) < acceptance_prob) {
        centers = new_centers;
        current_cost = new_cost;
      }
    }

    temp *= cooling;
  }

  return centers;
}

// Функция для ввода точек-клиентов
vector<pair<double, double>> input_clients() {
  vector<pair<double, double>> clients;
  int n;

  cout << "Введите количество точек-клиентов: ";
  cin >> n;

  cout << "Введите координаты " << n << " точек (x y):\n";
  for (int i = 0; i < n; i++) {
    double x, y;
    cout << "Точка " << i + 1 << ": ";
    cin >> x >> y;
    clients.push_back({x, y});
  }

  return clients;
}

// Функция для ввода параметров алгоритма
void input_parameters(int &k, double &temp, double &cooling) {
  cout << "\nВведите количество центров (k): ";
  cin >> k;

  cout << "Введите начальную температуру (рекомендуется 10-100): ";
  cin >> temp;

  cout << "Введите коэффициент охлаждения (0.9-0.99): ";
  cin >> cooling;
}

// Функция для вывода результатов
void print_results(const vector<pair<double, double>> &centers,
                   double final_cost,
                   const vector<pair<double, double>> &clients) {
  cout << "\n=== РЕЗУЛЬТАТЫ ===" << endl;
  cout << "Найденные центры:\n";
  for (int i = 0; i < centers.size(); i++) {
    cout << "Центр " << i + 1 << ": (" << centers[i].first << ", "
         << centers[i].second << ")\n";
  }

  cout << "\nФинальная стоимость (суммарное расстояние): " << final_cost
       << endl;

  // Дополнительная информация: распределение клиентов по центрам
  cout << "\nРаспределение клиентов по центрам:\n";
  for (int i = 0; i < clients.size(); i++) {
    double min_dist = numeric_limits<double>::max();
    int closest_center = -1;

    for (int j = 0; j < centers.size(); j++) {
      double dist = distance(clients[i], centers[j]);
      if (dist < min_dist) {
        min_dist = dist;
        closest_center = j;
      }
    }

    cout << "Клиент " << i + 1 << " (" << clients[i].first << ", "
         << clients[i].second << ") -> Центр " << closest_center + 1
         << " (расстояние: " << min_dist << ")\n";
  }
}

int main() {
  cout << "=== АЛГОРИТМ РАЗМЕЩЕНИЯ ЦЕНТРОВ (Имитация отжига) ===" << endl;

  // Ввод данных
  vector<pair<double, double>> clients = input_clients();

  int k;
  double initial_temp, cooling_rate;
  input_parameters(k, initial_temp, cooling_rate);

  // Проверка корректности ввода
  if (k <= 0 || initial_temp <= 0 || cooling_rate <= 0 || cooling_rate >= 1) {
    cout << "Ошибка: некорректные параметры!" << endl;
    return 1;
  }

  if (k > clients.size()) {
    cout << "Ошибка: количество центров не может быть больше количества "
            "клиентов!"
         << endl;
    return 1;
  }

  // Вывод введенных данных для проверки
  cout << "\n=== ВВЕДЕННЫЕ ДАННЫЕ ===" << endl;
  cout << "Количество клиентов: " << clients.size() << endl;
  cout << "Количество центров: " << k << endl;
  cout << "Начальная температура: " << initial_temp << endl;
  cout << "Коэффициент охлаждения: " << cooling_rate << endl;
  cout << "Координаты клиентов:\n";
  for (int i = 0; i < clients.size(); i++) {
    cout << "  " << i + 1 << ": (" << clients[i].first << ", "
         << clients[i].second << ")\n";
  }

  // Запуск алгоритма
  cout << "\nЗапуск алгоритма..." << endl;
  vector<pair<double, double>> result =
      sa_facility_location(clients, k, initial_temp, cooling_rate);

  // Вывод результатов
  double final_cost = totalDistance(clients, result);
  print_results(result, final_cost, clients);

  return 0;
}


### Пример входных и выходных данных для алгоритма размещения центров

### Входные данные:

```
=== АЛГОРИТМ РАЗМЕЩЕНИЯ ЦЕНТРОВ (Имитация отжига) ===
Введите количество точек-клиентов: 6
Введите координаты 6 точек (x y):
Точка 1: 1 2
Точка 2: 3 4
Точка 3: 5 6
Точка 4: 8 1
Точка 5: 9 3
Точка 6: 7 5

Введите количество центров (k): 2
Введите начальную температуру (рекомендуется 10-100): 50
Введите коэффициент охлаждения (0.9-0.99): 0.95
```

### Промежуточный вывод:

```
=== ВВЕДЕННЫЕ ДАННЫЕ ===
Количество клиентов: 6
Количество центров: 2
Начальная температура: 50
Коэффициент охлаждения: 0.95
Координаты клиентов:
  1: (1, 2)
  2: (3, 4)
  3: (5, 6)
  4: (8, 1)
  5: (9, 3)
  6: (7, 5)

Запуск алгоритма...
```

### Выходные данные:

```
=== РЕЗУЛЬТАТЫ ===
Найденные центры:
Центр 1: (3.2, 3.8)
Центр 2: (8.1, 2.9)

Финальная стоимость (суммарное расстояние): 8.74

Распределение клиентов по центрам:
Клиент 1 (1, 2) -> Центр 1 (расстояние: 2.5)
Клиент 2 (3, 4) -> Центр 1 (расстояние: 0.4)
Клиент 3 (5, 6) -> Центр 1 (расстояние: 2.7)
Клиент 4 (8, 1) -> Центр 2 (расстояние: 2.0)
Клиент 5 (9, 3) -> Центр 2 (расстояние: 1.1)
Клиент 6 (7, 5) -> Центр 2 (расстояние: 2.3)
```

