import matplotlib.pyplot as plt
import networkx as nx
"""
В якості вузлів реальної мережі візьмемо список міст, через які може пролягати популярний маршрут Київ-Буковель
В в якості ребер будуть автодороги між цими містами.
"""
# K - Київ
# G - Житомир
# T - Тернопіль
# R - Рівне
# H - Хмельницький
# L - Львів
# I - Івано-Франківськ
# B - Буковель

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

G = nx.Graph(graph)

print(f'Вершини графа: {G.nodes()}')
print(f'Кількість вершин: {G.number_of_nodes()}')

print(f'Ребра графа: {G.edges()}')
print(f'Кількість ребер: {G.number_of_edges()}')
print(f'Ступінь вершин: {G.degree()}')

plt.figure(figsize=(8, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=16, font_weight="bold")
plt.show()