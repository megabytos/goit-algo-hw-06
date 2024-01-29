from collections import deque

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ') 
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def bfs_recursive(graph, queue, visited=None):    
    if visited is None:
        visited = set()    
    if not queue:
        return   
    vertex = queue.popleft()    
    if vertex not in visited:       
        print(vertex, end=" ")        
        visited.add(vertex)        
        queue.extend(set(graph[vertex]) - visited)    
    bfs_recursive(graph, queue, visited)


graph = {
    "K": ["G"],
    "G": ["K", "R", "H"],
    "R": ["G", "T", "L"],
    "H": ["G", "T", "B"],
    "T": ["R", "H", "I"],
    "L": ["R", "I"],    
    "I": ["L", "T", "B"],
    "B": ["I"],
}

print("DFS: ", end="") 
dfs_recursive(graph, 'K')
print("\nBFS: ", end="") 
bfs_recursive(graph, deque(["K"]))