import tkinter as tk
from PIL import Image, ImageTk
import time

# Maze grid data and walls
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Define start and end
start = (1, 1)
end = (10, 10)

# Pathfinding - Depth First Search
def dfs(maze, start, end):
    stack = [(start, [start])]
    visited = set()

    while stack:
        (x, y), path = stack.pop()

        if (x, y) == end:
            return path

        if (x, y) not in visited:
            visited.add((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                    stack.append(((nx, ny), path + [(nx, ny)]))
    return []

# GUI Setup
class MazeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Solver")

        self.canvas = tk.Canvas(self.root, width=450, height=450)
        self.canvas.pack()

        self.cell_size = 30
        self.draw_maze()

        self.solve_button = tk.Button(self.root, text="Solve", command=self.solve_maze)
        self.solve_button.pack()

    def draw_maze(self):
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                color = "black" if maze[i][j] == 1 else "white"
                self.canvas.create_rectangle(j * self.cell_size, i * self.cell_size,
                                             (j + 1) * self.cell_size, (i + 1) * self.cell_size,
                                             fill=color, outline="gray")

        # Mark start and end
        self.canvas.create_oval(start[1] * self.cell_size + 5, start[0] * self.cell_size + 5,
                                (start[1] + 1) * self.cell_size - 5, (start[0] + 1) * self.cell_size - 5,
                                fill="blue")
        self.canvas.create_oval(end[1] * self.cell_size + 5, end[0] * self.cell_size + 5,
                                (end[1] + 1) * self.cell_size - 5, (end[0] + 1) * self.cell_size - 5,
                                fill="red")

    def solve_maze(self):
        path = dfs(maze, start, end)
        if path:
            self.animate_path(path)
        else:
            print("No solution found")

    def animate_path(self, path):
        for (x, y) in path:
            self.canvas.create_oval(y * self.cell_size + 10, x * self.cell_size + 10,
                                    (y + 1) * self.cell_size - 10, (x + 1) * self.cell_size - 10,
                                    fill="green")
            self.root.update()
            time.sleep(0.2)

# Main function
def main():
    root = tk.Tk()
    app = MazeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
