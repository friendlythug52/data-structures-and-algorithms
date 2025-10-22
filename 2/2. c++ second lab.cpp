#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Создание мультисписка (вектора векторов)
    vector<vector<int>> multiList = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    
    cout << "Мультисписок:" << endl;
    for (const auto& row : multiList) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
    
    // Добавление нового подсписка
    multiList.push_back({10, 11, 12});
    cout << "\nПосле добавления:" << endl;
    for (const auto& row : multiList) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
    
    // Обращение к элементам
    cout << "\nЭлемент [1][2]: " << multiList[1][2] << endl; // 6
    cout << "Элемент [0][0]: " << multiList[0][0] << endl; // 1
    
    // Изменение элемента
    multiList[2][1] = 88;
    cout << "\nПосле изменения [2][1]: ";
    for (int val : multiList[2]) {
        cout << val << " ";
    }
    cout << endl;
    
    // Зубчатый мультисписок
    vector<vector<int>> jaggedList = {
        {1, 2},
        {3, 4, 5, 6},
        {7},
        {8, 9, 10}
    };
    
    cout << "\nЗубчатый мультисписок:" << endl;
    for (const auto& row : jaggedList) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
    
    return 0;
}
