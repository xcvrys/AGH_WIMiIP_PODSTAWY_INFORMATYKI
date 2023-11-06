# 
# File name: zad3.py
# Author: Kamil Ryś
# Date created: 04.10.2023
# Task submited: 04.10.2023
# Last modified: 06.10.2023 <- day fixing the file size issue after new array.txt file was uploaded
#

import os
import time

def load_array_from_file(filename: str) -> list[int]:
  with open(filename, 'r') as file:
    data = file.read().strip()
  arr = list(map(int, data.split(';')))
  return arr

def calculate_sums(arr: list[int]) -> list[int]:
  total_sum = sum(arr)
  sums = [total_sum]
  
  for i in range(0, len(arr)):
    total_sum -= arr[i]
    sums.append(total_sum)
  
  return sums

if __name__ == "__main__":
  filename = 'array.txt'

  os.system('cls')
  show = input("Show array? [y/n]: ").lower() == 'y'


  calc_start = time.time()
  arr = load_array_from_file(filename)
  calced = calculate_sums(arr)
  calc_end = time.time()

  if show: print(calced)
  print("\033[92m{}\033[00m".format(f'Calculation took {(calc_end - calc_start) * 1000:.2f} ms to run.'))

