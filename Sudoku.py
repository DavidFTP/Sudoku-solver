import os
import time as t
import math as m

with open('in.txt') as f:
  stringBoard = f.read()
rows = stringBoard.split('\n')
b = [row.split(' ') for row in rows]

SIZE = int((len(rows[0]) + 1) / 2)
MOD = int(m.sqrt(SIZE) )

def makeBoard():
  for r in range(SIZE):
    for c in range(SIZE):
      if ord(b[r][c]) < 65:
        b[r][c] = int(b[r][c])
      else:
        b[r][c] = int(ord(b[r][c]) - 65 + 10)

def printBoard():
  hiphens = 2 * SIZE + (2 * MOD - 3)
  for r in range(SIZE):
    if r != 0 and r % MOD == 0:
      print('-'*hiphens, end='\n')
    for c in range(SIZE):
      if c != 0 and c % MOD == 0:
        print('|', end=" ")
      if b[r][c] > 9:
        if b[r][c] == 10: print('A', end=" ")
        if b[r][c] == 11: print('B', end=" ")
        if b[r][c] == 12: print('C', end=" ")
        if b[r][c] == 13: print('D', end=" ")
        if b[r][c] == 14: print('E', end=" ")
        if b[r][c] == 15: print('F', end=" ")
        if b[r][c] == 16: print('G', end=" ")
      else:
        print(b[r][c], end=" ")
    print()

def validNum(r, c, n): # Stands for the row, column and the number to be checked 
  row = False
  column = False
  Box = False
  for i in range(SIZE):
    if b[r][i] == n:
      row = True
  for i in range(SIZE):
    if b[i][c] == n:
      column = True
  rCounter = r - (r % 4)
  cCounter = c - (c % 4)
  for i in range(rCounter, rCounter + MOD):
    for j in range(cCounter, cCounter + MOD):
      if b[i][j] == n:
        Box = True
  return not row and not column and not Box
  
def solve():
  # counter = 0
  for row in range(SIZE):
    for column in range(SIZE):
      if b[row][column] == 0:
        for i in range(1, SIZE + 1):
          if validNum(row, column, i):
            # if counter % 10000 == 0:
            #   os.system('cls')
            #   printBoard()
            # counter += 1
            b[row][column] = i
            solve()
            b[row][column] = 0
        return False
  print("------------------------------------\nSolved:")
  printBoard()
  input()

makeBoard()
printBoard()
solve()
