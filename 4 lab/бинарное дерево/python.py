class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def find_path(self, target):
        path = []
        self._find_path_recursive(self.root, target, path)
        return path if path else None
    
    def _find_path_recursive(self, node, target, path):
        if node is None:
            return False
        
        path.append(node.value)
        
        if node.value == target:
            return True
        
        if (self._find_path_recursive(node.left, target, path) or 
            self._find_path_recursive(node.right, target, path)):
            return True
        
        path.pop()
        return False

# Пример использования
if __name__ == "__main__":
    tree = BinaryTree()
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    
    for value in values:
        tree.insert(value)
    
    print("Inorder обход:", tree.inorder_traversal())
    print("Поиск 6:", "Найден" if tree.search(6) else "Не найден")
    print("Поиск 20:", "Найден" if tree.search(20) else "Не найден")
    print("Путь к 13:", tree.find_path(13))
    print("Путь к 25:", tree.find_path(25))
