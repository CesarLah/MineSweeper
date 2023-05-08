#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This program is a game to find mines in a grid, that will give us how many mines are
# around the position on the grid.

# The functions created for the program are the following 
def create_grid(rows, columns):
    grid = [["-" for i in range(columns)] for j in range(rows)]       
    return grid

def fill_grid(num1, num2):
    grid[num1-1][num2-1] = "#"
    return grid

# Below are the different functions to check if there is a mine around the position i, j
def diagonal(i, j):
    # Checking if there is a mine in the diagonal position of i, j
    z = 0
    if grid[i+1][j+1] == "#":
        z +=1
    return z

def adjacent(i, j):
    z = 0
    if grid[i][j+1] == "#":
        z += 1
    return z

def below(i, j):
    z = 0
    if grid[i+1][j] == "#":
        z += 1
    return z

def below_reverse_diag(i, j):
    z = 0
    if grid[i+1][j-1] == "#":
        z += 1
    return z

def anterior(i, j):
    z = 0
    if grid[i][j-1] == "#":
        z += 1
    return z

def above(i, j):
    z = 0
    if grid[i-1][j] == "#":
        z += 1
    return z

def upper_diagonal(i, j):
    z = 0
    if grid[i-1][j+1] == "#":
        z += 1
    return z

def upper_reverse_diag(i, j):
    z = 0
    if grid[i-1][j-1] == "#":
        z = 1
    return z

# Main function of this program, to check every position surrounding the element i, j.
def minesweep():
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if (i == 0 and j == 0):                     # Upper left
                up_l = 0
                up_l = diagonal(i, j)
                up_l += adjacent(i, j)
                up_l += below(i, j)
                change_char(i, j, up_l)     
            if (i == 0 and (len(row) - 1) > j > 0):     # First row
                row_0 = 0
                row_0 = diagonal(i, j)
                row_0 += adjacent(i, j)
                row_0 += below(i, j)
                row_0 += below_reverse_diag(i, j)
                row_0 += anterior(i, j)
                change_char(i, j, row_0)
            if (i == 0 and j == (len(row) - 1)):        # Upper right        
                up_r = 0
                up_r += anterior(i, j)
                up_r += below_reverse_diag(i, j)
                up_r += below(i, j)
                change_char(i, j, up_r)
            if (0 < i < (len(grid)-1) and j == 0):      # First column
                col_0 = 0
                col_0 += below(i, j)
                col_0 += diagonal(i, j)
                col_0 += adjacent(i, j)
                col_0 += above(i, j)
                col_0 += upper_diagonal(i, j)
                change_char(i, j, col_0)
            if (0 < i < (len(grid) -1) and (0 < j < (len(row) - 1))):   # Middle of the grid
                mid = 0
                mid += below(i, j)
                mid += diagonal(i, j)
                mid += adjacent(i, j)
                mid += above(i, j)
                mid += upper_diagonal(i, j)
                mid += upper_reverse_diag(i, j)
                mid += anterior(i, j)
                mid += below_reverse_diag(i, j)
                change_char(i, j, mid)
            if (0 < i < (len(grid)-1) and j == (len(row)-1)):           # Last column
                col_n = 0
                col_n += above(i, j)
                col_n += anterior(i, j)
                col_n += below(i, j)
                col_n += upper_reverse_diag(i, j)
                col_n += below_reverse_diag(i, j)
                change_char(i, j, col_n)
            if (i == (len(grid)-1) and j == 0):                         # Bottom left
                bl = 0
                bl += upper_diagonal(i, j)
                bl += above(i, j)
                bl += adjacent(i, j)
                change_char(i, j, bl)
            if (i == (len(grid)-1) and (0 < j < (len(row)-1))):         # Last row
                row_n = 0
                row_n += upper_diagonal(i, j)
                row_n += upper_reverse_diag(i, j)
                row_n += above(i, j)
                row_n += anterior(i, j)
                row_n += adjacent(i, j)
                change_char(i, j, row_n)
            if (i == (len(grid)-1) and (j == (len(row)-1))):            # Bottom right
                br = 0
                br += above(i, j)
                br += anterior(i, j)
                br += upper_reverse_diag(i, j) 
                change_char(i, j, br)
    return grid

# Finally the function that will display the number of mines around
def change_char(i, j, x):
    if grid[i][j] == "-":
        grid[i][j] = str(x)
        return grid

# Main code block of the script
while True:
    rows = input("\nHow many rows you want the grid to have? (minimum 2): > ").strip(" ")
    columns = input("\nHow many columns you want the grid to have? (minimum 2): > ").strip(" ")
    try:
        num_rows = int(rows)
        num_columns = int(columns)
        if (num_rows < 2 or num_columns < 2):
            print("\nNumber of rows or columns are too small, try a bigger grid.")
            continue
        break
    except ValueError:
        print("\nYou haven't entered a number in one or both inputs. Try again.")
        continue
    
grid = create_grid(num_rows, num_columns)

pos = ""
while pos != "0":
    pos = input(f"""\nWhich positions do you want the mines to be at?\n(Example: 1,3 -> first row, third column) 
(from 1,1 to {rows},{columns}). 0 to exit: > """).strip(" ")
    if pos != "0":
        positions = pos.split(",")
        try:
            num1 = int(positions[0])
            num2 = int(positions[1])
            if (num1 > num_rows or num2 > num_columns):
                print("\nThis position is outside of the grid, try again.")
                continue
            fill_grid( num1, num2) 
        except ValueError:
            print("\nThese positions are not recognizable. Try again.")
            continue
        
print ("\nThis is the grid that you have created:")    
for row in grid:
    print(row)      
          
minesweep()

print("\nAnd this is the solution:")
for row in grid:
    print(row)


