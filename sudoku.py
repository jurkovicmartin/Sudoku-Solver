import numpy as np

class Sudoku():
    """
    Board represents 2D matrix of sudoku values. Zeros represents empty cells.

    Parameters
    -----
    values: 2D matrix of values is expected
    """
    def __init__(self, size: int, matrix):
        self.size = size

        values = np.array(matrix)
        if values.shape == (self.size, self.size):
            self.board = values
        else:
            raise Exception("Wrong matrix values provided.")
        

    def __str__(self) -> str:
        return ('\n'.join([' '.join([str(number) for number in row]) for row in self.board]))
    

    def solve(self) -> list | None:
        """
        Solves the sudoku.

        Returns
        -----
        list: solution

        None: sudoku doesn't have a solution
        """
        if self.find_solution():
            return self.board
        else:
            return None


    def find_solution(self) -> bool:
        """"
        Finds solution using backtracking algorithm.

        Returns
        -----
        True: sudoku was successfully solved

        False: sudoku does't have a solution
        """
        for row in range(self.size):
            for col in range(self.size):
                # Find empty cell (0)
                if self.board[row][col] == 0:
                    # Trying numbers
                    for num in range(1, 10):
                        if self.validate_value(row, col, num):
                            # Insert valid number
                            self.board[row][col] = num
                            
                            # Recursively try to solve next cell
                            if self.find_solution():
                                return True
                            
                            # Set value back to 0 (backtrack)
                            self.board[row][col] = 0

                    # No number (1-9) cannot be inserted (trigger backtracking)
                    return False
        # There are no empty cells
        return True

    

    def validate_value(self, row: int, column: int, value: int) -> bool:
        """"
        Validates if the value can be placed in that cell[row][column].

        Returns True if the value is valid.
        """
        if self.check_row(row, value):
            return False
        
        if self.check_column(column, value):
            return False
        
        if self.check_box(row, column, value):
            return False
        
        return True
    

    def check_row(self, row: int, value: int) -> bool:
        """
        Returns True if the row contains the value.
        """
        return value in self.board[row]
    

    def check_column(self, column: int, value: int) -> bool:
        """
        Returns True if the column contains the value.
        """
        for row in self.board:
            if row[column] == value:
                return True
        return False
    

    def check_box(self, row: int, column: int, value: int) -> bool:
        """
        Checks 3x3 box for the value.

        Returns True if the box contains the value.

        Parameters
        ------
        row, column indexes of current cell (box which contains this cell is checked.)
        """
        # Determine first cell of 3x3 box
        box_row = row // 3 * 3
        box_col = column // 3 * 3

        # Rows
        for x in range(3):
            # Columns
            for y in range(3):
                if self.board[box_row + x][box_col + y] == value:
                    return True
        return False