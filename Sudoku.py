import random
import tkinter as tk
from tkinter import messagebox

class Sudoku:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.board = [[0] * 9 for _ in range(9)]
        self.generate_board()
        self.create_grid()

    def generate_board(self):
        # تولید تخته کامل سودوکو
        self.fill_values()    # Fill the board with values
        self.remove_elements()  # Remove some elements to create the puzzle

    def fill_values(self):
        # پر کردن تخته با اعداد تصادفی
        self.solve_sudoku()  # Solve the Sudoku to generate a complete board
    
    def solve_sudoku(self):
        # حل کردن سودوکو با الگوریتم بازگشتی
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    random_numbers = list(range(1, 10))
                    random.shuffle(random_numbers)
                    for num in random_numbers:
                        if self.is_safe(i, j, num):
                            self.board[i][j] = num
                            if self.solve_sudoku():
                                return True
                            self.board[i][j] = 0
                    return False
        return True

    def is_safe(self, row, col, num):
        # بررسی ایمن بودن قرار دادن عدد در خانه
        for x in range(9):
            if self.board[row][x] == num or self.board[x][col] == num:
                return False
        
        start_row = row - row % 3
        start_col = col - col % 3
        
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
                    return False
        return True

    def remove_elements(self):
        # حذف برخی از اعداد برای ایجاد معما
        count = 40  # تعداد خانه‌هایی که باید خالی شوند
        while count > 0:
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            if self.board[i][j] != 0:
                self.board[i][j] = 0
                count -= 1

    def create_grid(self):
        self.entries = [[None] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.root, width=2, font=('Arial', 24), justify='center')
                entry.grid(row=i, column=j)
                if self.board[i][j] != 0:
                    entry.insert(0, str(self.board[i][j]))
                    entry.config(state='readonly')  # غیرقابل ویرایش
                self.entries[i][j] = entry

    def check_solution(self):
        # تابع برای بررسی حل سودوکو
        for i in range(9):
            row = [self.entries[i][j].get() for j in range(9)]
            if not self.is_valid(row):
                return False
        
        for j in range(9):
            col = [self.entries[i][j].get() for i in range(9)]
            if not self.is_valid(col):
                return False

        # بررسی مربع‌های کوچک
        for box_i in range(3):
            for box_j in range(3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(self.entries[box_i * 3 + i][box_j * 3 + j].get())
                if not self.is_valid(box):
                    return False

        return True

    def is_valid(self, values):
        # بررسی صحت مقادیر
        values = [v for v in values if v != '']
        return len(values) == len(set(values))

    def show_solution(self):
        # نمایش پیام حل موفقیت‌آمیز یا وجود خطا در حل
        if self.check_solution():
            messagebox.showinfo("Sudoku", "Congratulations! You solved it!")
        else:
            messagebox.showerror("Sudoku", "There are errors in your solution.")

