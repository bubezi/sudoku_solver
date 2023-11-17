import time
from functools import wraps


def time_this(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, "ETC:", end-start)
        return result
    return wrapper
    
x = 'y'
puzzle = [
    [5,3,x, x,7,x, x,x,x],
    [6,x,x, 1,9,5, x,x,x],
    [x,9,8, x,x,x, x,6,x],

    [8,x,x, x,6,x, x,x,3],
    [4,x,x, 8,x,3, x,x,1],
    [7,x,x, x,2,x, x,x,6],

    [x,6,x, x,x,x, 2,8,x],
    [x,x,x, 4,1,9, x,x,5],
    [x,x,x, x,8,x, x,7,9],
]


# puzzle = [
#     [5,3,4, 6,7,8, 9,1,2], 
#     [6,7,2, 1,9,5, 3,4,8], 
#     [1,9,8, 3,4,2, 5,6,7], 
#     [8,5,9, 7,6,1, 4,2,3], 
#     [4,2,6, 8,5,3, 7,9,1], 
#     [7,1,3, 9,2,4, 8,5,6], 
#     [9,6,1, 5,3,7, 2,8,4], 
#     [2,8,7, 4,1,9, 6,3,5], 
#     [3,4,5, 2,8,6, 1,7,9],
# ]


def convert_blank_to_x(puzzle):
    '''
    Function that converts all blanks to the string 'x'
    '''
    puzzle_sol = []
    for i in range(9):
        row = []
        for j in range(9):
            val = puzzle[i][j]
            if type(val) != int:
                val = 'x'
            row.append(val)
        puzzle_sol.append(row)
    return puzzle_sol


def sums_of_squares(puzzle):
    '''
    Function that calculates the sum of each 3 by 3 square 
    and returns a dictionary with the key as the square 
    number, moving from right to left and the sums as the 
    dictionary value
    '''
    puzzle = convert_blank_to_x(puzzle)
    sums_of_square = {}
    square = 0
    for start_x in [0, 3, 6]:
        for start_y in [0, 3, 6]:
            square_sum = 0
            for i in range(3):
                for j in range(3):
                    val = puzzle[start_x+i][start_y+j]
                    if val != 'x':
                        square_sum += val
            sums_of_square[square]=square_sum       
            square += 1
    return sums_of_square


def sums_of_rows_and_cols(puzzle):
    '''
    Function that calculates the sum of each row and column 
    and returns two dictionaries with the keys as the 
    row/column number and the sums as the value.
    '''
    puzzle = convert_blank_to_x(puzzle)
    sums_row = {}
    sums_col = {}
    for i in range(9):
        row_sum = 0
        col_sum = 0
        for j in range(9):
            val = puzzle[i][j]
            val_n = puzzle[j][i]
            if val != 'x':
                row_sum += val
            if val_n != 'x':
                col_sum += val_n
        sums_row[i]=row_sum
        sums_col[i]=col_sum
    return sums_row, sums_col


def sum_of_row(row, puzzle):
    '''
    Function that calculates the sum of a row
    and returns the sum as an interger.

    Takes in the row: int, and a puzzle[][] variable

    Depends on sums_of_rows_and_cols()
    '''
    r, c = sums_of_rows_and_cols(puzzle)
    return r[row]


def sum_of_col(col, puzzle):
    '''
    Function that calculates the sum of a column
    and returns the sum as an interger.

    Takes in the column: int, and a puzzle[][] variable

    Depends on sums_of_rows_and_cols()
    '''
    r, c = sums_of_rows_and_cols(puzzle)
    return c[col]


def sum_of_square(square, puzzle):
    '''
    Function that calculates the sum of a square
    and returns the sum as an interger.

    Takes in the square: int, and a puzzle[][] variable

    Depends on sums_of_squares()
    '''
    return sums_of_squares(puzzle)[square]


def convert_into_squares(puzzle):
    '''
    Takes in puzzle[][] and returns a dictionary with 
    the key as the square number, moving from right 
    to left and a list with the values in the square 
    as the dictionary value
    '''
    puzzle = convert_blank_to_x(puzzle)
    puzzle_new = {}
    square = 0
    for start_x in [0, 3, 6]:
        for start_y in [0, 3, 6]:
            square_items = []
            for i in range(3):
                for j in range(3):
                    val = puzzle[start_x+i][start_y+j]
                    square_items.append(val)
            puzzle_new[square]=square_items   
            square += 1
    return puzzle_new


def check_square_for_match(num, square, puzzle):
    puzzle = convert_into_squares(puzzle)
    for val in puzzle[square]:
        if val == num:
            return True
    return False 


def check_row_for_match(num, row, puzzle):
    puzzle = convert_blank_to_x(puzzle)
    for i in range(9):
        if puzzle[row][i] == num:
            return True
    return False


def check_col_for_match(num, col, puzzle):
    puzzle = convert_blank_to_x(puzzle)
    for i in range(9):
        if puzzle[i][col] == num:
            return True
    return False


def solved(puzzle):
    """
    Checks if the sudoku puzzle is solved and returns 
    False if the checks fail.
    """
    r, c = sums_of_rows_and_cols(puzzle)
    for i in range(9):
        if r[i]!=45:
            return False
        if c[i]!=45:
            return False
        if sum_of_square(i)!=45:
            return False
    return True


@time_this
def solve(puzzle):
    sol = puzzle
    while not solved(sol):
        print("Solving...")
        for row in range(9):
            for col in range(9):
                if type(sol[row][col]) != int:
                    for num in range(9):
                        if not check_row_for_match(num, row, sol):
                            pass
        # break
    print("Solved!!!")
    return sol


# solution = solve(puzzle)
# print(check_col_for_match(5, 4, puzzle))
