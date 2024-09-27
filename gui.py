import customtkinter as ctk
from tkinter import messagebox

from sudoku import Sudoku

class Gui(ctk.CTk):
    def __init__(self, size):
        super().__init__()
        self.size = size

        self.geometry("600x600")
        self.title("Sudoku solver")

        self.title = ctk.CTkLabel(self, height=100, text="SUDOKU SOLVER", font=("Helvetica", 48),
                                   fg_color="dark cyan", corner_radius=25)
        self.title.pack(padx=5, pady=5, fill="x")

        self.game_frame = ctk.CTkFrame(self)
        self.game_frame.pack(padx=5, pady=5)

        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.pack(padx=5, pady=5)

        self.grid_frames =[]

        # Create frames for 3x3 cells
        for i in range(self.size // 3):
            for j in range(self.size // 3):
                frame = ctk.CTkFrame(self.game_frame, width=120, height=120)
                frame.grid(row=i, column=j, padx=3, pady=3)
                self.grid_frames.append(frame)

        
        valid_cmd = (self.register(self.validate_input), "%P")
        self.cells = [[None for _ in range(self.size)] for _ in range(self.size)]

        # Create cells
        for index, frame in enumerate(self.grid_frames):
            frame_row = index // 3
            frame_col = index % 3

            for i in range(3):
                for j in range(3):
                    cell_row = frame_row * 3 + i
                    cell_col = frame_col * 3 + j

                    entry = ctk.CTkEntry(frame, width=35, height=35, font=("Helvetica", 22), justify="center",
                                         validate="key", validatecommand=valid_cmd)
                    entry.grid(row=i, column=j, padx=1, pady=1)

                    self.cells[cell_row][cell_col] = entry
        

        self.solve_btn = ctk.CTkButton(self.buttons_frame, text="SOLVE", font=("Helvetica", 26), fg_color="dark cyan", command=self.submit_values)
        self.solve_btn.grid(row=0, column=0, padx=5, pady=5)

        self.clear_btn = ctk.CTkButton(self.buttons_frame, text="CLEAR", font=("Helvetica", 26), fg_color="dark cyan", command=self.clear_input)
        self.clear_btn.grid(row=0, column=1, padx=5, pady=5)

        self.quit_btn = ctk.CTkButton(self.buttons_frame, text="QUIT", font=("Helvetica", 26), fg_color="dark cyan", command=self.destroy)
        self.quit_btn.grid(row=0, column=2, padx=5, pady=5)


    def submit_values(self):
        self.get_input()

        sudoku = Sudoku(self.size, self.values)
        solution = sudoku.solve()

        if solution is None:
            messagebox.showerror("Solution status", "This sudoku does't have a solution. Check input values.")
            return
        
        for row_num, row in enumerate(self.cells):
            for cell_num, cell in enumerate(row):
                cell.delete(0)
                cell.insert(0, str(solution[row_num][cell_num]))
                cell.configure(state="disabled")


    def get_input(self):
        """
        Get values from entries and saves them to an list.
        """
        self.values = []

        for row in self.cells:
            values_row = []
            for cell in row:
                value = cell.get()
                if value == "":
                    values_row.append(0)
                else:
                    values_row.append(int(value))
            self.values.append(values_row)


    def validate_input(self, value: str) -> bool:
        """
        For validating Entries input values (only one digit number and not zero).
        """
        if value == "":
            return True
        elif value.isdigit():
            if len(value) == 1:
                return value != "0"
            else:
                return False
        else:
            return False
        
    
    def clear_input(self):
        for row in self.cells:
            for cell in row:
                cell.configure(state="normal")
                cell.delete(0)