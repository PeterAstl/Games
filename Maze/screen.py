
import tkinter as tk
import turtle
from PIL import Image, ImageTk
from player import *

class Screen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Maze")
        self.root.geometry("800x800")
        self.width = 800
        self.height = 800

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("white")
        self.pen = turtle.RawTurtle(self.screen)
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.size = 25
        self.pen.color("grey")
        self.pen.shape("square")
        self.pen.shapesize(self.size/20)
        self.start = [1,1]
        self.bg_image = ""
        self.image()
        img = Image.open("Relaxo.png")
        img = img.resize((self.size, self.size))
        img.save("Relaxo.gif")
        self.screen.addshape("Relaxo.gif")

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
                    self.pen.color("green")
                    self.pen.stamp()
                    self.pen.color("grey")
                    self.start = [x * self.size + offset_x, y * self.size + offset_y]

                if maze[x, y]["end"]:
                    self.pen.goto(x * self.size + offset_x, y * self.size + offset_y)
                    self.pen.color("blue")
                    self.pen.stamp()
                    self.pen.color("grey")

                else:
                    if not maze[x, y]["wall"] and not maze[x, y]["end"] and not maze[x, y]["start"]:
                        random_enemy_amount = random.randint(1,20)
                        if random_enemy_amount == 1:
                            self.pen.goto(x * self.size + offset_x, y * self.size + offset_y)
                            self.pen.shape("Relaxo.gif")
                            self.pen.stamp()
                            self.pen.shape("square")
                            maze[x, y]["enemy"] = True
                    if not maze[x, y]["wall"] and not maze[x, y]["end"] and not maze[x, y]["start"] and not maze[x, y]["enemy"]:
                        random_item_amount = random.randint(1, 20)
                        if random_item_amount == 1:
                            self.pen.goto(x * self.size + offset_x, y * self.size + offset_y)
                            self.pen.color("lightgreen")
                            self.pen.stamp()
                            self.pen.color("grey")
                            maze[x,y]["item"] = True

    def image(self):
        image = Image.open("background.jpg")
        image = image.resize((self.width, self.height))
        self.bg_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="center")

    def start_position(self):
        return self.start
