#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <limits>
#include <algorithm>

class Dijkstra {
private:
    std::unordered_map<std::string, std::unordered_map<std::string, int>> graph;

public:
    Dijkstra(const std::unordered_map<std::string, std::unordered_map<std::string, int>>& g) 
        : graph(g) {}
    
    std::pair<int, std::vector<std::string>> shortestPath(const std::string& start, const std::string& end) {
        // Инициализация расстояний
        std::unordered_map<std::string, int> distances;
        for (const auto& node : graph) {
            distances[node.first] = std::numeric_limits<int>::max();
        }
        distances[start] = 0;
        
        // Приоритетная очередь
        using Pair = std::pair<int, std::string>;
        std::priority_queue<Pair, std::vector<Pair>, std::greater<Pair>> priority_queue;
        priority_queue.push({0, start});
        
        // Для восстановления пути
        std::unordered_map<std::string, std::string> previous;
        
        while (!priority_queue.empty()) {
            auto [current_distance, current_node] = priority_queue.top();
            priority_queue.pop();
            
            // Если достигли конечной вершины
            if (current_node == end) {
                break;
            }
            
            // Если текущее расстояние больше сохраненного, пропускаем
            if (current_distance > distances[current_node]) {
                continue;
            }
            
            // Обновляем расстояния до соседей
            for (const auto& neighbor : graph[current_node]) {
                int distance = current_distance + neighbor.second;
                
                if (distance < distances[neighbor.first]) {
                    distances[neighbor.first] = distance;
                    previous[neighbor.first] = current_node;
                    priority_queue.push({distance, neighbor.first});
                }
            }
        }
        
        // Восстанавливаем путь
        std::vector<std::string> path;
        std::string current = end;
        
        while (previous.find(current) != previous.end()) {
            path.push_back(current);
            current = previous[current];
        }
        path.push_back(start);
        std::reverse(path.begin(), path.end());
        
        return {distances[end], path};
    }
};

int main() {
    // Граф в виде словаря смежности
    std::unordered_map<std::string, std::unordered_map<std::string, int>> graph = {
        {"A", {{"B", 4}, {"C", 2}}},
        {"B", {{"A", 4}, {"D", 5}, {"E", 8}}},
        {"C", {{"A", 2}, {"D", 8}, {"E", 3}}},
        {"D", {{"B", 5}, {"C", 8}, {"E", 1}, {"F", 6}}},
        {"E", {{"B", 8}, {"C", 3}, {"D", 1}, {"F", 4}}},
        {"F", {{"D", 6}, {"E", 4}}}
    };
    
    Dijkstra dijkstra(graph);
    
    std::string start = "A";
    std::string end = "F";
    auto [distance, path] = dijkstra.shortestPath(start, end);
    
    std::cout << "Кратчайшее расстояние от " << start << " до " << end << ": " << distance << std::endl;
    std::cout << "Путь: ";
    for (size_t i = 0; i < path.size(); ++i) {
        std::cout << path[i];
        if (i < path.size() - 1) {
            std::cout << " -> ";
        }
    }
    std::cout << std::endl;
    
    // Все кратчайшие расстояния от A
    std::cout << "\nВсе кратчайшие расстояния от A:" << std::endl;
    for (const auto& node : graph) {
        auto [dist, _] = dijkstra.shortestPath(start, node.first);
        std::cout << "До " << node.first << ": " << dist << std::endl;
    }
    
    return 0;
}
