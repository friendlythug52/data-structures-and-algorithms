class FibonacciHeap:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.degree = 0
            self.marked = False
            self.parent = None
            self.child = None
            self.left = self
            self.right = self
    
    def __init__(self):
        self.min_node = None
        self.count = 0
    
    def is_empty(self):
        return self.min_node is None
    
    def insert(self, key, value):
        node = self.Node(key, value)
        if self.min_node is None:
            self.min_node = node
        else:
            self._add_to_root_list(node)
            if key < self.min_node.key:
                self.min_node = node
        self.count += 1
        return node
    
    def _add_to_root_list(self, node):
        node.left = self.min_node
        node.right = self.min_node.right
        self.min_node.right.left = node
        self.min_node.right = node
    
    def find_min(self):
        return self.min_node.value if self.min_node else None
    
    def extract_min(self):
        if self.is_empty():
            return None
        
        min_node = self.min_node
        if min_node.child:
            child = min_node.child
            while True:
                next_child = child.right
                self._add_to_root_list(child)
                child.parent = None
                if next_child == min_node.child:
                    break
                child = next_child
        
        min_node.left.right = min_node.right
        min_node.right.left = min_node.left
        
        if min_node == min_node.right:
            self.min_node = None
        else:
            self.min_node = min_node.right
            self._consolidate()
        
        self.count -= 1
        return min_node.value
    
    def _consolidate(self):
        if not self.min_node:
            return
        
        degree_table = {}
        nodes = []
        current = self.min_node
        
        while True:
            nodes.append(current)
            current = current.right
            if current == self.min_node:
                break
        
        for node in nodes:
            degree = node.degree
            while degree in degree_table:
                other = degree_table[degree]
                if node.key > other.key:
                    node, other = other, node
                self._link(other, node)
                del degree_table[degree]
                degree += 1
            degree_table[degree] = node
        
        self.min_node = None
        for node in degree_table.values():
            if self.min_node is None or node.key < self.min_node.key:
                self.min_node = node
    
    def _link(self, child, parent):
        child.left.right = child.right
        child.right.left = child.left
        
        child.parent = parent
        if parent.child is None:
            parent.child = child
            child.left = child
            child.right = child
        else:
            child.left = parent.child
            child.right = parent.child.right
            parent.child.right.left = child
            parent.child.right = child
        
        parent.degree += 1
        child.marked = False

# Пример использования
if __name__ == "__main__":
    print("Куча Фибоначчи (Python):")
    fib_heap = FibonacciHeap()
    
    fib_heap.insert(5, "A")
    fib_heap.insert(3, "B")
    fib_heap.insert(8, "C")
    fib_heap.insert(1, "D")
    
    print("Минимальный элемент:", fib_heap.find_min())
    print("Извлеченные элементы:")
    while not fib_heap.is_empty():
        print(fib_heap.extract_min(), end=" ")
    print()
