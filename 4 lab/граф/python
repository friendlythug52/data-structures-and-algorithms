from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(dict)
    
    def add_edge(self, u, v, weight=1):
        self.adj_list[u][v] = weight
        self.adj_list[v][u] = weight  # Для неориентированного графа
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        visited = set()
        result = []
        self._dfs_recursive(start, visited, result)
        return result
    
    def _dfs_recursive(self, vertex, visited, result):
        visited.add(vertex)
        result.append(vertex)
        
        for neighbor in self.adj_list[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited, result)
    
    def get_edges(self):
        edges = []
        for u in self.adj_list:
            for v, weight in self.adj_list[u].items():
                if u < v:  # Чтобы избежать дублирования в неориентированном графе
                    edges.append((u, v, weight))
        return edges

# Пример использования
if __name__ == "__main__":
    graph = Graph()
    
    # Добавление рёбер
    edges = [
        ('A', 'B', 4), ('A', 'C', 2),
        ('B', 'D', 5), ('C', 'D', 8),
        ('C', 'E', 3), ('D', 'E', 1),
        ('D', 'F', 6), ('E', 'F', 4)
    ]
    
    for u, v, weight in edges:
        graph.add_edge(u, v, weight)
    
    print("BFS обход от A:", graph.bfs('A'))
    print("DFS обход от A:", graph.dfs('A'))
    print("Рёбра графа:", graph.get_edges())
