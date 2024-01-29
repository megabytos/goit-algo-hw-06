import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):    
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:        
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])        
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight            
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


graph = {
    "K": {"G": 140},
    "G": {"K": 140, "R": 180, "H": 190},    
    "R": {"G": 180, "T": 150, "L": 210},
    "H": {"G": 190, "T": 110, "B": 330},    
    "T": {"R": 150, "H": 110, "I": 130,},
    "L": {"R": 210, "I": 130},
    "I": {"L": 130, "T": 130, "B": 90},
    "B": {"I": 90},
}

print('Найкоротші відстані від "K" до інших міст (км)')
print(dijkstra(graph, 'K'))

G = nx.Graph()
G.add_edge('K', 'G', weight=140)
G.add_edge('G', 'R', weight=180)
G.add_edge('G', 'H', weight=190)
G.add_edge('R', 'L', weight=210)
G.add_edge('R', 'T', weight=150)
G.add_edge('H', 'T', weight=110)
G.add_edge('L', 'I', weight=130)
G.add_edge('T', 'I', weight=130)
G.add_edge('I', 'B', weight=90)
G.add_edge('H', 'B', weight=340)

print('Найкоротші шляхи від "K" до інших міст')
print(nx.single_source_dijkstra_path(G, 'K'))
# print(nx.single_source_dijkstra_path_length(G, 'K'))

plt.figure(figsize=(8, 8))
pos = nx.spring_layout(G, seed=31)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=16, font_weight="bold", width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()