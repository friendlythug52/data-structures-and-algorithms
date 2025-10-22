#include <iostream>
#include <vector>
#include <memory>

class TreeNode {
public:
    int value;
    std::unique_ptr<TreeNode> left;
    std::unique_ptr<TreeNode> right;
    
    TreeNode(int val) : value(val), left(nullptr), right(nullptr) {}
};

class BinaryTree {
private:
    std::unique_ptr<TreeNode> root;
    
    void insertRecursive(TreeNode* node, int value) {
        if (value < node->value) {
            if (node->left == nullptr) {
                node->left = std::make_unique<TreeNode>(value);
            } else {
                insertRecursive(node->left.get(), value);
            }
        } else if (value > node->value) {
            if (node->right == nullptr) {
                node->right = std::make_unique<TreeNode>(value);
            } else {
                insertRecursive(node->right.get(), value);
            }
        }
    }
    
    TreeNode* searchRecursive(TreeNode* node, int value) const {
        if (node == nullptr || node->value == value) {
            return node;
        }
        if (value < node->value) {
            return searchRecursive(node->left.get(), value);
        }
        return searchRecursive(node->right.get(), value);
    }
    
    void inorderRecursive(TreeNode* node, std::vector<int>& result) const {
        if (node != nullptr) {
            inorderRecursive(node->left.get(), result);
            result.push_back(node->value);
            inorderRecursive(node->right.get(), result);
        }
    }
    
    bool findPathRecursive(TreeNode* node, int target, std::vector<int>& path) const {
        if (node == nullptr) {
            return false;
        }
        
        path.push_back(node->value);
        
        if (node->value == target) {
            return true;
        }
        
        if (findPathRecursive(node->left.get(), target, path) || 
            findPathRecursive(node->right.get(), target, path)) {
            return true;
        }
        
        path.pop_back();
        return false;
    }

public:
    BinaryTree() : root(nullptr) {}
    
    void insert(int value) {
        if (root == nullptr) {
            root = std::make_unique<TreeNode>(value);
        } else {
            insertRecursive(root.get(), value);
        }
    }
    
    bool search(int value) const {
        return searchRecursive(root.get(), value) != nullptr;
    }
    
    std::vector<int> inorderTraversal() const {
        std::vector<int> result;
        inorderRecursive(root.get(), result);
        return result;
    }
    
    std::vector<int> findPath(int target) const {
        std::vector<int> path;
        if (findPathRecursive(root.get(), target, path)) {
            return path;
        }
        return {};
    }
};

int main() {
    BinaryTree tree;
    std::vector<int> values = {8, 3, 10, 1, 6, 14, 4, 7, 13};
    
    for (int value : values) {
        tree.insert(value);
    }
    
    std::cout << "Inorder обход: ";
    auto traversal = tree.inorderTraversal();
    for (int val : traversal) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    
    std::cout << "Поиск 6: " << (tree.search(6) ? "Найден" : "Не найден") << std::endl;
    std::cout << "Поиск 20: " << (tree.search(20) ? "Найден" : "Не найден") << std::endl;
    
    auto path = tree.findPath(13);
    std::cout << "Путь к 13: ";
    for (int val : path) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
