# 
# File name: zad5.py
# Author: Kamil Ryś
# Date created: 04.10.2023
# Task submited: 05.10.2023
# Last modified: 11.10.2023 fixed `calculate_average_point_of_nearby_sectors` function counting all sectors with not existing 
#

import os
from random import randint

def generate_sectors_matrix(n: int) -> list[list[int]]:
  return [[randint(0, 2500) for _ in range(n)] for _ in range(n)]

def generate_points_matrix(matrix: list[int]) -> list[list[int]]:
  return [[0 for _ in range(len(matrix) + 1)] for _ in range(len(matrix) + 1)]

# Old more complex solution counting only sectors touching the point
# def calculate_average_point_of_nearby_sectors(sectors: list[list[int]], points: list[list[int]]) -> list[list[float]]:
#   n = len(sectors)
#   for i in range(n + 1):
#     for j in range(n + 1):
#       sectors_touched = []
#       if i > 0 and j > 0:
#         sectors_touched.append(sectors[i - 1][j - 1])
#       if i > 0 and j < n:
#         sectors_touched.append(sectors[i - 1][j])
#       if i < n and j > 0:
#         sectors_touched.append(sectors[i][j - 1])
#       if i < n and j < n:
#         sectors_touched.append(sectors[i][j])
#       average = sum(sectors_touched) / len(sectors_touched)
#       points[i][j] = average
#   return points

# New simplified solution counting all sectors around the point even if they don't exist
def calculate_average_point_of_nearby_sectors(sectors: list[list[int]], points: list[list[int]]) -> list[list[float]]:
  n = len(sectors)

  for i in range(n + 1):
    for j in range(n + 1):
      total = 0

      for x in range(i - 1, i + 1):
        for y in range(j - 1, j + 1):
          if 0 <= x < n and 0 <= y < n:
            total += sectors[x][y]

      average_value = total / 4
      points[i][j] = average_value

  return points

def colorit(func):
  def wrapper(*args, **kwargs):
    print("\033[92m")
    result = func(*args, **kwargs)
    print("\033[00m")
    return result
  return wrapper

@colorit
def main(matrix: list[list[int]]):
  print('points:', *calculate_average_point_of_nearby_sectors(matrix, generate_points_matrix(matrix)), sep='\n')

if __name__ == '__main__':
  os.system('cls')
  matrix_size = input('Enter matrix size (or -1 to exit): ')
  if matrix_size == '-1':
    exit()
  matrix_size = int(matrix_size)
  matrix = generate_sectors_matrix(matrix_size)
  print('sectors:', *matrix, sep='\n')
  main(matrix)
