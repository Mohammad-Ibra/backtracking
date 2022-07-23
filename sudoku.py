### A function that checks if the number assigned is safe
def is_safe(grid, pos_x, pos_y, num):
    ### It checks the column
    for i in range(9):
        if pos_y<9 and grid[i][pos_y] == num:
            return False
    ### It checks the row
    for i in range(9):
        if pos_x<9 and grid[pos_x][i] == num:
            return False
    
    ### It checks the box
    for i in range(3):
        for j in range(3):
            if 0<= i + pos_x - pos_x%3<9 and 0<=j + pos_y - pos_y%3<9 and grid[i + pos_x - pos_x%3][j + pos_y - pos_y%3] == num:
                return False
    
    return True

### A function that checks for empty slots in the grid and assigns its position to the l list.
def is_empty(grid, l):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False

def solve(grid):
    ### a list that contains the position x and y
    ### It is initialized at the position (0,0)

    l = [0,0]

    ### Base case: There is no empty slots in the grid
    if not is_empty(grid, l):
        return True

    pos_x = l[0]
    pos_y = l[1]

    ### Iterate between possible solutions from 1 to 9
    for i in range(1,10):
        ### Check if the number meets the constraints
        if is_safe(grid, pos_x, pos_y, i):
            ### Assign the number to its position
            grid[pos_x][pos_y] = i
            ### Checks if this number leads to a solution
            if solve(grid):
                return True
            ### Backtrack if it does not lead to a solution by 
            ### giving a value of 0 to its position
            grid[pos_x][pos_y] = 0

    ### Backtrack to the previous num if none of the 9 possible solutions work
    ### If there is no solution it will return False
    return False

### A utility function that prints the grid
def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()

def main():
    grid = [
         [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] 
    ]
    if solve(grid):
        print_grid(grid)
    else:
        print("There is no solution that exists")

if __name__ == "__main__":
    main()


    