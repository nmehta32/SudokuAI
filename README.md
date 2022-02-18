# SudokuAI
Using CSP and Backtracking to solve Sudoku
\\

FUNCTIONS

Input_Data() = Takes and reads a file converting the to a certain layout. 

Plot() = takes cols a string of numbers and rows a string of integer to form a grid

__init__() = a constructor for our class

get_rows() = going through rows making a lists with cols. ([A1, A2, A3, etc], [B1, B2, etc]

get_cols() = going through cols making a lists with rows. ([A1, B2, C3, etc], [A2, B2, C2, etc]

get_box() = getting the every 3 in a row and col. ([A1, A2, A3, B1, B2, B3, C1, C2, C3], {A4, etc)

addTogether() = adds the functions get_rows, get_cols, and get_box together

get_grid() = making a dictionary that stores information from addTogether with each information from sudokuGrid. (A1: [['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'], etc ])

get_a() = find things that is in one set but not in the other. ('A1': {'B3', 'A2', 'A5', 'C1', etc})

get_constriants() = it shows where the constraints. 

matrix() = it looks through the graph and fills it values

rev() = it checks the sudoku to see if the changes are still following the rules

AC3() = it is using ac3 method to check to see if the program is consistent.

isComplete() = checks to see if the sudoku has been all filled if not return false else return true

safe() = checks to see if there is a 0 in our sudoku

used() = to check to see if there is the same number used in a row, col, or box

solve_sudoku() = to solve sudoku by calling other functions

parseGrid() =  print out the sudoku after we solve it.







Consistency check functions
__init__()
get_rows()
get_cols()
get_box()
addTogether()
get_Grid
get_a()
get_constriants() 
matrix()
rev()
isComplete()


Backtracking Functions
 Solve_sudoku()
 Used()
 Safe()
