## Dimensions of the chessboard
N = 8
## Possible moves of a knight on a chessboard, X and Y coordinates
moves_x = [2,1,-1,-2,-2,-1,1,2]
moves_y = [1,2,2,1,-1,-2,-2,-1]
## Initialize the board
board = [[-1 for i in range(N)] for _ in range(N)]

def is_safe(grid, x, y) -> bool:
    """
    x: position x of the knight on the board
    y: position y of the knight on the board
    grid: The board

    return
    ------
    True: if the cell is not  out of border, or not visited already
    """
    if 0 <= x < N and 0 <= y < N and grid[x][y] == -1:
        return True
    return False

def backtrack(grid, cur_x, cur_y, move_count):
    """
    grid: the board
    cur_x: current position x of the knight
    cur_y: current position y of the knight
    move_count: keeps track of the number of moves
    
    return
    ------
    True: at the end of the call stack
    """

    ### Base case: If all moves are done
    if move_count >= N*N:
        return True

    ### Consider all possible moves
    for i in range(8):
        next_x = cur_x + moves_x[i]
        next_y = cur_y + moves_y[i]

        ###Check if this move can be considered
        if is_safe(grid, next_x, next_y):
            ### take this move
            grid[next_x][next_y] = move_count

            ### Check if this move lead to a solution from all recur moves
            if backtrack(grid, next_x, next_y, move_count+1):
                return True

            ###This move did not work, backtrack
            grid[next_x][next_y] = -1

    ### No move from the 8 worked, so we backtrack and we retry from the previous move and re-try
    return False

### A generic function that prints the board
def print_grid(grid):
    for i in range(N):
        for j in range(N):
            print(grid[i][j], end=" ")
        print()

def main():
    board[0][0] = 0   # Start with the knight Initially at the first bloack
    backtrack(board, 0, 0, 1)
    print_grid(board)

if __name__ == "__main__":
    main()


    