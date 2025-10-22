#include <iostream>
#include <vector>
#include <algorithm>

class BinaryHeap {
private:
    std::vector<int> heap;

    void heapify_up(int index) {
        while (index > 0 && heap[parent(index)] > heap[index]) {
            std::swap(heap[parent(index)], heap[index]);
            index = parent(index);
        }
    }

    void heapify_down(int index) {
        int smallest = index;
        int left = left_child(index);
        int right = right_child(index);

        if (left < heap.size() && heap[left] < heap[smallest])
            smallest = left;
        if (right < heap.size() && heap[right] < heap[smallest])
            smallest = right;

        if (smallest != index) {
            std::swap(heap[index], heap[smallest]);
            heapify_down(smallest);
        }
    }

    int parent(int i) { return (i - 1) / 2; }
    int left_child(int i) { return 2 * i + 1; }
    int right_child(int i) { return 2 * i + 2; }

public:
    void push(int value) {
        heap.push_back(value);
        heapify_up(heap.size() - 1);
    }

    int pop() {
        if (heap.empty()) return -1;
        
        int root = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        heapify_down(0);
        return root;
    }

    int peek() {
        return heap.empty() ? -1 : heap[0];
    }

    bool is_empty() {
        return heap.empty();
    }

    size_t size() {
        return heap.size();
    }
};

int main() {
    BinaryHeap heap;
    std::vector<int> data = {8, 3, 5, 1, 6, 2, 4, 7};

    std::cout << "Бинарная куча (C++):" << std::endl;
    for (int num : data) {
        heap.push(num);
    }

    while (!heap.is_empty()) {
        std::cout << heap.pop() << " ";
    }
    std::cout << std::endl;
    return 0;
}
