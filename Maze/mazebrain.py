import random
from screen import *

class Maze:
    def __init__(self, width, height):
        self.maze = {}
        self.height = height
        self.width = width
        self.direction = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        self.screen = Screen()

    def mix(self):
        for y in range(self.height):
            for x in range(self.width):
                self.maze[x, y] = {
                    "wall": True,
                    "visited": False,
                    "start" : False,
                    "end": False,
        }
        ex = self.width -3
        ey = self.height -3
        self.maze[(ex, ey)]["end"] = True
        self.maze[(ex, ey)]["wall"] = False

        # erzeugt den Start bei 1,1
        self.carve(1,1)
        self.maze[1, 1]["start"] = True

    def carve(self, x, y):
        #entfernt wand von nicht besuchtem feld
        self.maze[(x, y)]["wall"] = False
        self.maze[(x, y)]["visited"] = True

        random.shuffle(self.direction)

        for dx, dy in self.direction:
            nx, ny = x + dx, y + dy

            if self.is_valid(nx, ny) and not self.maze[(nx, ny)]["visited"]:
                wx, wy = x + dx // 2, y + dy // 2
                self.maze[(wx, wy)]["wall"] = False
                self.carve(nx, ny)

    def draw(self):
        self.screen.paint(self.maze, self.height, self.width)

    def is_valid(self, x, y):
        return 0 <= x < self.width -1 and 0 <= y < self.height -1

    def maze_clear(self):
        self.maze = {}
        self.screen.pen.clear()
        self.height = random.randrange(11, 31, 2)
        self.width = random.randrange(11, 31, 2)
        self.mix()
        self.draw()

