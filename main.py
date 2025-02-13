import tkinter as tk
from Sudoku import Sudoku
if __name__ == "__main__":
    root = tk.Tk()
    sudoku_game = Sudoku(root)
    check_button = tk.Button(root, text="Check Solution", command=sudoku_game.show_solution)
    
check_button.grid(row=9, columnspan=9)
root.mainloop()