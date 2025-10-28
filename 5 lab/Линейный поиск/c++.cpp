#include <iostream>
#include <vector>
using namespace std;

int linearSearch(const vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

int main() {
    vector<int> arr = {3, 5, 2, 7, 9, 1, 4};
    int target = 7;
    int result = linearSearch(arr, target);
    
    if (result != -1) {
        cout << "Элемент найден на позиции: " << result << endl;
    } else {
        cout << "Элемент не найден" << endl;
    }
    return 0;
}
