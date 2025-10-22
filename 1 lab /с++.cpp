#include <iostream>
#include <stack>

int main() {
    std::stack<std::string> stack;
    stack.push("a");
    stack.push("b");
    stack.push("c");
    
    // Для вывода нужно скопировать стек
    std::stack<std::string> temp = stack;
    while(!temp.empty()) {
        std::cout << temp.top() << " ";
        temp.pop();
    }
    std::cout << std::endl;
    
    return 0;
}
