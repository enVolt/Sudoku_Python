# Sudoku_Python
Python Script to create a solved Sudoku 

As for now, this is not working, either it is leading to Invalid Block, 
or I'm being ended up Puzzle with more than one solution

Here is my logic to create puzzle

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Count = 0

Board[9][9] = 0.....0 

while Count < 82:
  Find possible solutions for all positions
  For all pos, where only one number can be placed, fill that number # no such case for empty board
  If no such number in found in above step:
    Choose a random position (i,j)
    Fill any random number on Board[i][j], such that it should be legal move
    # Move is legal, if no. doesn't exist in row, column, and mini-block
