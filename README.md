# BACKTRACKING

**BackTracking** works in an incremental way to tackle problems.
The steps involved in the backtracking algorithm are:

1. Start from an empty solution vector. 
2. We then add solutions to the victor. 
3. The solutions should always respect the constraints of the problem. 
4. If the constraints are violated, we remove the solution from the vector and we try other alternatives. 
5. If all the alternatives do not work, we return back to the previous stage and remove it. 
6. If we reach the initial stage without solutions existing, we say that there is no solutions.
7. If adding an item does not violate the constraints, we then recursively add to the vector until the solution is complete. 

**Examples of backtracking algorithms:**
- The knight's tour problem
- Rat in a maze
- N queen problem
- Subset sum
- m Coloring problem
- Hamiltonian cycle
- sudoku solver
- solving Cryptarithmetic Puzzles
- Magnet puzzle

### The knight's tour problem

**Setting up the problem**

Given an N*N board with the knight placed on the first block of an empty board. Moving according to the rules of the chess knight
must visit each square exactly once. Print the order of each cell in which they are visited. 

**Example**

```
    Input: 
    N = 8
```

```
    Output: 
    0  59  38  33  30  17   8  63
    37  34  31  60   9  62  29  16
    58   1  36  39  32  27  18   7
    35  48  41  26  61  10  15  28
    42  57   2  49  40  23   6  19
    47  50  45  54  25  20  11  14
    56  43  52   3  22  13  24   5
    51  46  55  44  53   4  21  12
```

The logic behind the backtracking algorithm for the knight's tour problem:

```
if all squares are visited:
    print the solution
else:
    a. Add one of the next moves to the solution vector and recursively check if this move lead to a solution.
    (A knight can make a maximum of 8 moves. We choose of these 8 moves in this step.)
    b. If the move chosen in the above step doesn't lead to a solution then remove this move from the solution vector and try other alternative moves.
    c. If none of the alternatives work then return false (Returning false will remove the previously added item in recursion and if false is returned by the initial call of recursion then "no solution exists"
```

### Rat in a maze

**Setting up the problem**

A rat starts from source and has to reach the destination. The rat can move to up, down, right and left. In the maze matrix, 0 means the block is a dead end and 1 means the block can be used in the path from source to destination

**Example**

```
    Input:
    [
        [1,0,0,0],
        [1,1,0,1],
        [0,1,0,0],
        [1,1,1,1],
    ]
```
```
    Output:
    [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,1],
    ]
```

The logic behind the backtracking algorithm of the rat in a maze problem is:

```
The approach is to form a recursive function, which will follow a path and checks if the path reaches the destination or not.
If the path does not reach the destination then backtrack and try other paths. 

1. create a solution matrix initially filled with 0s.
2. create a recursive function which takes the initial matrix and returns matrix and position of the rat.
3. If the position is out of the matrix or not valid, then return.
4. Mark the position output[i][j] as 1 and check if the current position is destination or not. If destination is reached print the output matrix and return.
5. Recursively call for position (i-1,j), (I,j-1), (i+1, j) and (i, j+1)
6. Unmark position (i, j), i.e output[i][j] = 0.
```

### N queen problem

**Setting up the problem**

The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.

**Example**

```
    Input:
    N = 4
```
```
    Output:
    [
        [0,1,0,0],
        [0,0,0,1],
        [1,0,0,0],
        [0,0,1,0]
    ]
```

The idea is to place queens one by one in different columns, starting from the leftmost column. When we place a queen in a column, we check for clashes with already placed queens. In the current column, if we find a row for which there is no clash, we mark this row and column as part of the solution. If we do not find such a row due to clashes, then we backtrack and return false.

The logic behind the backtracking algorithm for the N-queens problem is:

```
1. Start in the leftmost column.
2. If all queen are placed return True.
3. Try all rows in the current column. 
    For every tried row we do the following:
    a. If the queen can be placed safely in this row 
       then mark this [row, column] as part of the 
       solution and recursively check if placing
       queen here leads to a solution.
    b. If placing the queen in [row, column] leads to
       a solution then return true.
    c. If placing queen doesn't lead to a solution then
       unmark this [row, column] (Backtrack) and go to 
       step (a) to try other rows.
4. If all rows have been tried and nothing worked,
   return false to trigger backtracking.
```
### Subset Sum

**Setting up the problem**

Given a non-empty array of positive integer, find the subset where its sum is equal to a desired outcome. It is assumed that the 
input set is unique. (No duplicates are presented.)

**Example**

```
    Input:
    nums = [1,5,4,11]
    sum = 10
```
```
    Output:
    [1,5,4]
```

The logic behind the backtracking algorithm for the subset sum problem is:

```
1. Start with an empty set
2. Add the next element from the list to the set
3. If the subset is having sum M, then stop with that subset as a solution.
4. If the subset is not feasible, or if we have reached the end of the set, then backtrack through the subset until we find the most suitable solution.
5. If the subset is feasible (sum of subset < M>) then repeat step 2.
6. If we have visited all elements without finding a suitable solution and if no backtracking is feasible, then there is no solution. 
```

### Sudoku

**Setting up the problem**

Given a partially filled 9×9 2D array ‘grid[9][9]’, the goal is to assign digits (from 1 to 9) to the empty cells so that every row, column, and subgrid of size 3×3 contains exactly one instance of the digits from 1 to 9. 

**Example**

```
    Input:
    {
         {3, 0, 6, 5, 0, 8, 4, 0, 0}, 
         {5, 2, 0, 0, 0, 0, 0, 0, 0}, 
         {0, 8, 7, 0, 0, 0, 0, 3, 1}, 
         {0, 0, 3, 0, 1, 0, 0, 8, 0}, 
         {9, 0, 0, 8, 6, 3, 0, 0, 5}, 
         {0, 5, 0, 0, 9, 0, 6, 0, 0}, 
         {1, 3, 0, 0, 0, 0, 2, 5, 0}, 
         {0, 0, 0, 0, 0, 0, 0, 7, 4}, 
         {0, 0, 5, 2, 0, 6, 3, 0, 0} 
    }
```
```
    Output:
    3 1 6 5 7 8 4 9 2
    5 2 9 1 3 4 7 6 8
    4 8 7 6 2 9 5 3 1
    2 6 3 4 1 5 9 8 7
    9 7 4 8 6 3 1 2 5
    8 5 1 7 9 2 6 4 3
    1 3 8 9 4 7 2 5 6
    6 9 2 3 5 1 8 7 4
    7 4 5 2 8 6 3 1 9
```

The logic behind the backtracking algorithm for sudoku is:

Sudoku can be solved by one by one assigning numbers to empty cells. Before assigning a number, check whether it is safe to assign. Check that the same number is not present in the current row, current column and current 3X3 subgrid. After checking for safety, assign the number, and recursively check whether this assignment leads to a solution or not. If the assignment doesn’t lead to a solution, then try the next number for the current empty cell. And if none of the number (1 to 9) leads to a solution, return false and print no solution exists.

```
1. Create a function that checks after assigning the current index the grid becomes unsafe or not. Keep Hashmap for a row, column and boxes. If any number has a frequency greater than 1 in the hashMap return false else return true; hashMap can be avoided by using loops.
2. Create a recursive function that takes a grid.
3. Check for any unassigned location. If present then assign a number from 1 to 9, check if assigning the number to current index makes the grid unsafe or not, if safe then recursively call the function for all safe cases from 0 to 9. if any recursive call returns true, end the loop and return true. If no recursive call returns true then return false.
4. If there is no unassigned location then return true.
```