import heapq
import math

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
    
    def shortest_path(self, start, end):
        # Инициализация расстояний
        distances = {node: math.inf for node in self.graph}
        distances[start] = 0
        
        # Приоритетная очередь
        priority_queue = [(0, start)]
        
        # Для восстановления пути
        previous = {}
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            # Если достигли конечной вершины
            if current_node == end:
                break
            
            # Если текущее расстояние больше сохраненного, пропускаем
            if current_distance > distances[current_node]:
                continue
            
            # Обновляем расстояния до соседей
            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        # Восстанавливаем путь
        path = []
        current = end
        
        while current in previous:
            path.append(current)
            current = previous[current]
        
        path.append(start)
        path.reverse()
        
        return distances[end], path

# Пример использования
if __name__ == "__main__":
    # Граф в виде словаря смежности
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'D': 5, 'E': 8},
        'C': {'A': 2, 'D': 8, 'E': 3},
        'D': {'B': 5, 'C': 8, 'E': 1, 'F': 6},
        'E': {'B': 8, 'C': 3, 'D': 1, 'F': 4},
        'F': {'D': 6, 'E': 4}
    }
    
    dijkstra = Dijkstra(graph)
    
    start = 'A'
    end = 'F'
    distance, path = dijkstra.shortest_path(start, end)
    
    print(f"Кратчайшее расстояние от {start} до {end}: {distance}")
    print(f"Путь: {' -> '.join(path)}")
    
    # Все кратчайшие расстояния от A
    print("\nВсе кратчайшие расстояния от A:")
    for node in graph:
        dist, _ = dijkstra.shortest_path(start, node)
        print(f"До {node}: {dist}")
