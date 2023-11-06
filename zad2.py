# 
# File name: zad2.py
# Author: Kamil Ryś
# Date created: 03.10.2023
# Last modified: 03.10.2023
#

import os

def caesar(text: str, shift: int, decrypt: bool) -> str:
  output = []
  for char in text:
    if char.isalpha():
      shifted = ord(char) - shift if decrypt else ord(char) + shift
      if char.islower():
        if shifted > ord('z'):
          shifted -= 26
        elif shifted < ord('a'):
          shifted += 26
      else:
        if shifted > ord('Z'):
          shifted -= 26
        elif shifted < ord('A'):
          shifted += 26
      output.append(chr(shifted))
    else:
      output.append(char)
  return ''.join(output)

def select() -> int:
  while True:
    print('1. Encrypt')
    print('2. Decrypt')
    print('3. Exit')
    print('0. Decrypt "FGHQVHWR VASBEZNGLXR GRPUAVPMAN"')
    option = input('Select option: ')
    
    if option == '0':
      print("\033[92m{}\033[00m".format(f'Decrypted text: {caesar("FGHQVHWR VASBEZNGLXR GRPUAVPMAN", 13, True)}\n'))
      continue

    if option in ['1', '2', '3']:
      return int(option)
    else:
      print("\033[91m{}\033[00m".format('Invalid option. Please choose 1, 2, or 3.\n'))


def gat_caesar_data(decrypt: bool) -> None:
  os.system('cls')
  text = input('Text to decrypt: ')
  shift = int(input('Shift: '))
  if decrypt:
    print("\033[92m{}\033[00m".format(f'Encrypted text: {caesar(text, shift, decrypt)}\n'))
  else:
    print("\033[92m{}\033[00m".format(f'Decrypted text: {caesar(text, shift, decrypt)}\n'))
  

if __name__ == '__main__':
  os.system('cls')
  while True:
    option = select()
    match option:
      case 1: gat_caesar_data(False)
      case 2: gat_caesar_data(True)
      case 3: break