from sudoku import Sudoku

from gui import Gui

def main():
    app = Gui(9)
    app.mainloop()

    # values = [[1, 0, 0, 4, 8, 9, 0, 0, 6],
    #          [7, 3, 0, 0, 5, 0, 0, 4, 0],
    #          [4, 6, 0, 0, 0, 1, 2, 9, 5],
    #          [3, 8, 7, 1, 2, 0, 6, 0, 0],
    #          [5, 0, 1, 7, 0, 3, 0, 0, 8],
    #          [0, 4, 6, 0, 9, 5, 7, 1, 0],
    #          [9, 1, 4, 6, 0, 0, 0, 8, 0],
    #          [0, 2, 0, 0, 4, 0, 0, 3, 7],
    #          [8, 0, 3, 5, 1, 2, 0, 0, 4]
    # ]

    # sudoku = Sudoku(values)
    
    # print(sudoku)
    # if sudoku.solve():
    #     print("Solved successfully.")
    #     print(sudoku)
    # else:
    #     print("Solution doesn't exist.")


if __name__ == "__main__":
    main()