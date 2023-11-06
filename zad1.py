# 
# File name: zad1.py
# Author: Kamil Ryś
# Date created: 04.10.2023
# Last modified: 04.10.2023
#

import os, random

def create_graph(num_vertices: int) -> list[list[int]]:
  return [[0] * num_vertices for _ in range(num_vertices)]

def graph_display(graph: list[list[int]]) -> None:
  for row in graph:
    print(row)

def assign_random_weights(graph: list[list[int]], min_weight: int, max_weight: int) -> None:
  for i in range(len(graph)):
    for j in range(i + 1, len(graph[i])):
      weight = random.randint(min_weight, max_weight)
      graph[i][j] = weight
      graph[j][i] = weight

def find_max_weight_edge(graph: list[list[int]]) -> None:
  max_weight = 0
  max_edge = None
  num_vertices = len(graph)

  for i in range(num_vertices):
    for j in range(i + 1, num_vertices):
      if graph[i][j] > max_weight:
        max_weight = graph[i][j]
        max_edge = (i, j)

  if max_edge is not None:
    print("\033[92m{}\033[00m".format(f"Highest weight: {max_edge[0], max_edge[1]}"))


if __name__ == '__main__':
  num_vertices = 5 # if max_egde[0] is all the time 0 it's beacaue of too small weight range OR `if graph[i][j] > max_weight:` isn't `>=``
  min_weight = 5
  max_weight = 25

  os.system('cls')
  graph = create_graph(num_vertices)
  assign_random_weights(graph, min_weight, max_weight)

  print("Graph after weight assing:")
  graph_display(graph)

  find_max_weight_edge(graph)
