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



