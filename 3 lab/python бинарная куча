import heapq

class BinaryHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        heapq.heappush(self.heap, item)
    
    def pop(self):
        return heapq.heappop(self.heap) if self.heap else None
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0

# Пример использования
if __name__ == "__main__":
    heap = BinaryHeap()
    data = [8, 3, 5, 1, 6, 2, 4, 7]
    
    for num in data:
        heap.push(num)
    
    print("Бинарная куча (Python):")
    while not heap.is_empty():
        print(heap.pop(), end=" ")
    print()
