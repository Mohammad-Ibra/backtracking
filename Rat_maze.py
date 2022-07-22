### Initialize a maze to travel
### 1 represents open paths and 0 represents closed paths
maze = [
        [1,0,0,0],
        [1,1,0,1],
        [0,1,0,0],
        [1,1,1,1],
    ]
### Initialize the destination
destination = [3,3]

### Initialize a solution array filled with 0s
solution = [[0 for _ in range(len(maze))] for i in range(len(maze[0])) ]

### The moves allowed for the rat (Left, Right, Down, Up)
move_x = [-1,1,0,0]
move_y = [0,0,-1,1]


def is_safe(pos_x, pos_y):
    """
    pos_x: position x of the rat
    pos_y: position y of the rat

    return:
    -------
    True: if it is an allowed move for the rat. (It is inside the maze, traversed for the first time and there is no wall)
    """
    if 0<=pos_x < len(maze) and 0<= pos_y< len(maze[0]) and maze[pos_x][pos_y] == 1 and solution[pos_x][pos_y] == 0:
        return True
    return False

### A generic function to print the path traveled inside the maze.
### 1 is where the rat passed
def print_solution():
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            print(int(solution[i][j]), end=" | ")
        print()

def travel(pos_x, pos_y):
    """
    pos_x: the current position x of the rat
    pos_y: the current position y of the rat

    return
    ------
    True When reaching the destination and False when no.
    """
    ### Base Case: We reached the destination, so we return True. 
    if pos_x == destination[0] and pos_y == destination[1]:
        return True

    ### Iterate through all the moves of the rat
    for i in range(4):

        x_new = pos_x + move_x[i]
        y_new = pos_y + move_y[i]

        ### Check if the current move is possible
        if is_safe(x_new, y_new):
            ### Take this move
            solution[x_new][y_new] = 1

            ### Check if the current move lead to a solution from all recur moves
            if travel(x_new, y_new):
                return True

            ### This move did not work, backtrack
            solution[x_new][y_new] = 0
    
    ### No move from the 4 worked so we backtrack and we retry from the previous move
    return False

def solve(pos_x, pos_y):
    solution[pos_x][pos_y] = 1

    if travel(pos_x, pos_y):
        print_solution()
    else:
        print("Solution does not exist!")

if __name__ == "__main__":
    solve(0,0)