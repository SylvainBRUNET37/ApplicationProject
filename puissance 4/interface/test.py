import tkinter as tk

class Puissance4:
    def __init__(self, root, rows=6, cols=7):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.board = [[0] * cols for _ in range(rows)]

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=self.cols * 50, height=self.rows * 50)
        self.canvas.pack()

        for i in range(1, self.cols):
            x = i * 50
            self.canvas.create_line(x, 0, x, self.rows * 50, fill="blue")

        for j in range(1, self.rows):
            y = j * 50
            self.canvas.create_line(0, y, self.cols * 50, y, fill="blue")

        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        col = event.x // 50
        row = event.y // 50

        if 0 <= row < self.rows and 0 <= col < self.cols:
            print(f"Clicked on column {col}, row {row}")

            # TODO: Add your logic for updating the game board here

            # Example: Draw a red circle representing a token
            x1, y1 = col * 50, row * 50
            x2, y2 = (col + 1) * 50, (row + 1) * 50
            self.canvas.create_oval(x1, y1, x2, y2, fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = Puissance4(root)
    root.mainloop()
