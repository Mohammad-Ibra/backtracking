n = 4
grid = [[0 for _ in range(n)] for i in range(n)]

def is_safe(row, col):

    # Check this row on left side
    for i in range(col):
        if grid[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), 
                    range(col, -1, -1)):
        if grid[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), 
                    range(col, -1, -1)):
        if grid[i][j] == 1:
            return False

    return True

def print_grid():
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()

def sum_elements():
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += grid[i][j]
    return sum

def solve(pos_y):
    
    if sum_elements() == n:
        return True


    for i in range(n):

        if is_safe(i, pos_y):

            grid[i][pos_y] = 1
            if solve(pos_y + 1):
                return True
            
            grid[i][pos_y] = 0
    
    return False

def main():
    solve(0)
    print_grid()

if __name__ == "__main__":
    main()

