#include <iostream>
#include <unordered_map>
#include <vector>
#include <cmath>

class FibonacciHeap {
private:
    struct Node {
        int key;
        std::string value;
        int degree;
        bool marked;
        Node* parent;
        Node* child;
        Node* left;
        Node* right;
        
        Node(int k, const std::string& v) 
            : key(k), value(v), degree(0), marked(false), 
              parent(nullptr), child(nullptr), left(this), right(this) {}
    };
    
    Node* min_node;
    int count;
    
    void add_to_root_list(Node* node) {
        node->left = min_node;
        node->right = min_node->right;
        min_node->right->left = node;
        min_node->right = node;
    }
    
    void link(Node* child, Node* parent) {
        child->left->right = child->right;
        child->right->left = child->left;
        
        child->parent = parent;
        if (!parent->child) {
            parent->child = child;
            child->left = child;
            child->right = child;
        } else {
            child->left = parent->child;
            child->right = parent->child->right;
            parent->child->right->left = child;
            parent->child->right = child;
        }
        
        parent->degree++;
        child->marked = false;
    }
    
    void consolidate() {
        if (!min_node) return;
        
        std::unordered_map<int, Node*> degree_table;
        std::vector<Node*> nodes;
        Node* current = min_node;
        
        do {
            nodes.push_back(current);
            current = current->right;
        } while (current != min_node);
        
        for (Node* node : nodes) {
            int degree = node->degree;
            while (degree_table.find(degree) != degree_table.end()) {
                Node* other = degree_table[degree];
                if (node->key > other->key) {
                    std::swap(node, other);
                }
                link(other, node);
                degree_table.erase(degree);
                degree++;
            }
            degree_table[degree] = node;
        }
        
        min_node = nullptr;
        for (auto& pair : degree_table) {
            Node* node = pair.second;
            if (!min_node || node->key < min_node->key) {
                min_node = node;
            }
        }
    }

public:
    FibonacciHeap() : min_node(nullptr), count(0) {}
    
    bool is_empty() const {
        return min_node == nullptr;
    }
    
    Node* insert(int key, const std::string& value) {
        Node* node = new Node(key, value);
        if (!min_node) {
            min_node = node;
        } else {
            add_to_root_list(node);
            if (key < min_node->key) {
                min_node = node;
            }
        }
        count++;
        return node;
    }
    
    std::string find_min() {
        return min_node ? min_node->value : "";
    }
    
    std::string extract_min() {
        if (is_empty()) return "";
        
        Node* min_node_ptr = min_node;
        if (min_node_ptr->child) {
            Node* child = min_node_ptr->child;
            do {
                Node* next_child = child->right;
                add_to_root_list(child);
                child->parent = nullptr;
                child = next_child;
            } while (child != min_node_ptr->child);
        }
        
        min_node_ptr->left->right = min_node_ptr->right;
        min_node_ptr->right->left = min_node_ptr->left;
        
        if (min_node_ptr == min_node_ptr->right) {
            min_node = nullptr;
        } else {
            min_node = min_node_ptr->right;
            consolidate();
        }
        
        count--;
        std::string result = min_node_ptr->value;
        delete min_node_ptr;
        return result;
    }
};

int main() {
    std::cout << "Куча Фибоначчи (C++):" << std::endl;
    FibonacciHeap fib_heap;
    
    fib_heap.insert(5, "A");
    fib_heap.insert(3, "B");
    fib_heap.insert(8, "C");
    fib_heap.insert(1, "D");
    
    std::cout << "Минимальный элемент: " << fib_heap.find_min() << std::endl;
    std::cout << "Извлеченные элементы: ";
    while (!fib_heap.is_empty()) {
        std::cout << fib_heap.extract_min() << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
