#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <string>

class Graph {
private:
    std::unordered_map<std::string, std::unordered_map<std::string, int>> adj_list;

public:
    void addEdge(const std::string& u, const std::string& v, int weight = 1) {
        adj_list[u][v] = weight;
        adj_list[v][u] = weight; // Для неориентированного графа
    }
    
    std::vector<std::string> bfs(const std::string& start) {
        std::vector<std::string> result;
        std::unordered_set<std::string> visited;
        std::queue<std::string> queue;
        
        visited.insert(start);
        queue.push(start);
        
        while (!queue.empty()) {
            std::string vertex = queue.front();
            queue.pop();
            result.push_back(vertex);
            
            for (const auto& neighbor : adj_list[vertex]) {
                if (visited.find(neighbor.first) == visited.end()) {
                    visited.insert(neighbor.first);
                    queue.push(neighbor.first);
                }
            }
        }
        
        return result;
    }
    
    std::vector<std::string> dfs(const std::string& start) {
        std::vector<std::string> result;
        std::unordered_set<std::string> visited;
        std::stack<std::string> stack;
        
        stack.push(start);
        
        while (!stack.empty()) {
            std::string vertex = stack.top();
            stack.pop();
            
            if (visited.find(vertex) == visited.end()) {
                visited.insert(vertex);
                result.push_back(vertex);
                
                for (const auto& neighbor : adj_list[vertex]) {
                    if (visited.find(neighbor.first) == visited.end()) {
                        stack.push(neighbor.first);
                    }
                }
            }
        }
        
        return result;
    }
    
    void printEdges() {
        std::cout << "Рёбра графа:" << std::endl;
        for (const auto& node : adj_list) {
            for (const auto& neighbor : node.second) {
                if (node.first < neighbor.first) { // Чтобы избежать дублирования
                    std::cout << node.first << " - " << neighbor.first 
                              << " (вес: " << neighbor.second << ")" << std::endl;
                }
            }
        }
    }
};

int main() {
    Graph graph;
    
    // Добавление рёбер
    graph.addEdge("A", "B", 4);
    graph.addEdge("A", "C", 2);
    graph.addEdge("B", "D", 5);
    graph.addEdge("C", "D", 8);
    graph.addEdge("C", "E", 3);
    graph.addEdge("D", "E", 1);
    graph.addEdge("D", "F", 6);
    graph.addEdge("E", "F", 4);
    
    auto bfs_result = graph.bfs("A");
    std::cout << "BFS обход от A: ";
    for (const auto& vertex : bfs_result) {
        std::cout << vertex << " ";
    }
    std::cout << std::endl;
    
    auto dfs_result = graph.dfs("A");
    std::cout << "DFS обход от A: ";
    for (const auto& vertex : dfs_result) {
        std::cout << vertex << " ";
    }
    std::cout << std::endl;
    
    graph.printEdges();
    
    return 0;
}
