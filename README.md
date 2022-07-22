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
    c. If none of the alternatives work then return false (Returning false will remove the previously added item in recursion and if false is returned by the initial call of recursion then "no solution exists")
```