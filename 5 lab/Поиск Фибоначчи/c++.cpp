#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int fibonacciSearch(const vector<int>& arr, int target) {
    int n = arr.size();
    
    int fib_m2 = 0;
    int fib_m1 = 1;
    int fib_m = fib_m2 + fib_m1;
    
    while (fib_m < n) {
        fib_m2 = fib_m1;
        fib_m1 = fib_m;
        fib_m = fib_m2 + fib_m1;
    }
    
    int offset = -1;
    
    while (fib_m > 1) {
        int i = min(offset + fib_m2, n - 1);
        
        if (arr[i] < target) {
            fib_m = fib_m1;
            fib_m1 = fib_m2;
            fib_m2 = fib_m - fib_m1;
            offset = i;
        } else if (arr[i] > target) {
            fib_m = fib_m2;
            fib_m1 = fib_m1 - fib_m2;
            fib_m2 = fib_m - fib_m1;
        } else {
            return i;
        }
    }
    
    if (fib_m1 && offset + 1 < n && arr[offset + 1] == target) {
        return offset + 1;
    }
    
    return -1;
}

int main() {
    vector<int> arr = {10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100};
    int target = 85;
    int result = fibonacciSearch(arr, target);
    
    if (result != -1) {
        cout << "Элемент найден на позиции: " << result << endl;
    } else {
        cout << "Элемент не найден" << endl;
    }
    return 0;
}
