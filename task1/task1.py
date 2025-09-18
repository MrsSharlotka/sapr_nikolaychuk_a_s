# task1
#
# Условие:
# Дан ориентированный ациклический граф G = (V, E), где:
#   V -- множество вершин графа,
#   E -- множество рёбер графа.
#
# Каждое ребро ei принадлежит E и описывается парой (vj, vk), где:
#   vj, vk принадлежит V -- вершины графа.
#
# Граф задаётся в виде CSV-файла. Каждая строка файла соответствует одному ребру:
#   начальная вершина, конечная вершина
#
# Пример входных данных (graph.csv):
# 1,2
# 1,3
# 3,4
# 3,5
#
# Задача:
# 1. Написать функцию
#       def main(csv_graph: str) -> list[list[int]]]:
#          ...
#    где csv_graph -- строка (содержимое CSV-файла).
#
# 2. Функция должна возвращать матрицу смежности графа в виде списка списков list[list].
#    - Размер матрицы: n x n, где n = |V| (количество вершин графа).
#    - Элемент matrix[i][j] равен 1, если существует ребро из вершины i в вершину j, и 0, если ребра нет.
#
# Ожидаемый результат:
#  [[0, 1, 1, 0, 0],
#   [1, 0, 0, 0, 0],
#   [1, 0, 0, 1, 1],
#   [0, 0, 1, 0, 0],
#   [0, 0, 1, 0, 0]]
from pathlib import Path
def main(csv_graph: str) -> list[list[int]]:
    with open(csv_graph, mode="r") as f:
        edges = [line.strip().split(',') for line in f.readlines()]
    
    edge_list = []
    vertices = set()
    for e in edges:
        u, v = map(int, e)
        edge_list.append((u, v))
        vertices.add(u)
        vertices.add(v)
    
    n = max(vertices)
    
    matrix = [[0] * n for _ in range(n)]
    
    for u, v in edge_list:
        matrix[u - 1][v - 1] = 1
    
    return matrix

print(main(Path(__file__).parent / 'csv_graph.csv'))