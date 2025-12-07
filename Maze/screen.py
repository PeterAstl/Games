
import tkinter as tk
import turtle

class Screen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Maze")
        self.root.geometry("800x800")

        self.canvas = tk.Canvas(self.root, width=800, height=800)
        self.canvas.pack()

        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("white")
        self.pen = turtle.RawTurtle(self.screen)
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.size = 18
        self.pen.color("turquoise")
        self.pen.shape("square")
        self.pen.shapesize(self.size/20)
        self.start = [1,1]

    def paint(self, maze, height, width):
        offset_x = round(-width * self.size /2)
        offset_y = round(-height * self.size /2)
        for y in range(height):
            for x in range(width):
                if maze[x, y]["wall"]:
                    self.pen.goto(x * self.size + offset_x, y * self.size + offset_y)
                    self.pen.stamp()
                if maze[x, y]["start"]:
                    self.pen.goto(x * self.size + offset_x, y * self.size + offset_y)
                    self.pen.color("red")
                    self.pen.stamp()
                    self.pen.color("turquoise")
                    self.start = [x * self.size + offset_x, y * self.size + offset_y]

                if maze[x, y]["end"]:
                    self.pen.goto(x * self.size + offset_x, y * self.size + offset_y)
                    self.pen.color("red")
                    self.pen.stamp()
                    self.pen.color("turquoise")


    def start_position(self):
        return self.start


