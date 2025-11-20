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
        
        // Критерий Метрополиса
        if (new_cost < current_cost) {
            // Всегда принимаем улучшающее решение
            centers = new_centers;
            current_cost = new_cost;
        } else {
            // Принимаем ухудшающее решение с вероятностью exp((current_cost - new_cost)/temp)
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
