# 
# File name: zad4.py
# Author: Kamil Ryś
# Date created: 04.10.2023
# Task submited: 04.10.2023
# Last modified: 11.10.2023 comment "nie rozpatrzono liczby 8902", code not changed - only screenshot attached
#

import os

def count_ones_bin(n: int) -> int:
  binary_str = bin(n)[2:]
  return binary_str.count('1')

def find_closest_greater_with_same_ones(n) -> int:
  if n <= 0:
    return None

  ones_count = count_ones_bin(n)

  greater_number = n + 1
  while count_ones_bin(greater_number) != ones_count:
    greater_number += 1

  return greater_number

if __name__ == '__main__':
  os.system('cls')
  print('Closest greater number with the same number of ones')  
  while True:
    try:
      input_number = int(input('Enter a number (or -1 to exit): '))
      if input_number == -1:
        break
      print("\033[92m{}\033[00m".format(f'Greater number of {input_number} is: \033[1m{find_closest_greater_with_same_ones(input_number)}'))

    except ValueError:
      print("\033[91m{}\033[00m".format('Invalid input. Please enter a valid number or -1 to exit.\n'))
