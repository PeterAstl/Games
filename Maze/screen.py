
import tkinter as tk
import turtle
from PIL import ImageTk
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
        if os.path.exists("pictures/Relaxo.png"):
            img = Image.open("pictures/Relaxo.png")
            img = img.resize((self.size, self.size))
            img.save("pictures/Relaxo.gif")
            self.screen.addshape("pictures/Relaxo.gif")
            self.enemy_exists = True
        else:
            self.enemy_exists = False
        if os.path.exists("pictures/sand.png"):
            img = Image.open("pictures/sand.png")
            img = img.resize((self.size, self.size))
            img.save("pictures/sand.gif")
            self.screen.addshape("pictures/sand.gif")
            self.wall_exists = True
        else:
            self.wall_exists = False
        if os.path.exists("pictures/chest.jpg"):
            img = Image.open("pictures/chest.jpg")
            img = img.resize((self.size, self.size))
            img.save("pictures/chest.gif")
            self.screen.addshape("pictures/chest.gif")
            self.chest_exists = True
        else:
            self.chest_exists = False
        if os.path.exists("pictures/loch.jpg"):
            img = Image.open("pictures/loch.jpg")
            img = img.resize((self.size, self.size))
            img.save("pictures/loch.gif")
            self.screen.addshape("pictures/loch.gif")
            self.loch_exists = True
        else:
            self.loch_exists = False


    def paint(self, maze, height, width):
        offset_x = round(-width * self.size /2)
        offset_y = round(-height * self.size /2)
        for y in range(height):
            for x in range(width):
                if maze[x, y]["wall"]:
                    self.pen.goto(x * self.size + offset_x, y * self.size + offset_y)
                    if self.wall_exists:
                        self.pen.shape("pictures/sand.gif")
                        self.pen.stamp()
                        self.pen.shape("square")
                    else:
                        self.pen.color("grey")
                        self.pen.stamp()
                if maze[x, y]["start"]:
                    self.start = [x * self.size + offset_x, y * self.size + offset_y]

                if maze[x, y]["end"]:
                    self.pen.goto(x * self.size + offset_x, y * self.size + offset_y)
                    if self.loch_exists:
                        self.pen.shape("pictures/loch.gif")
                        self.pen.stamp()
                    else:
                        self.pen.color("blue")
                        self.pen.stamp()

                else:
                    if not maze[x, y]["wall"] and not maze[x, y]["end"] and not maze[x, y]["start"]:
                        random_enemy_amount = random.randint(1,20)
                        if random_enemy_amount == 1:
                            self.pen.goto(x * self.size + offset_x, y * self.size + offset_y)
                            if self.enemy_exists:
                                self.pen.shape("pictures/Relaxo.gif")
                                maze[x,y]["id"] = self.pen.stamp()
                            else:
                                self.pen.color("red")
                                self.pen.stamp()
                            maze[x, y]["enemy"] = True
                    if not maze[x, y]["wall"] and not maze[x, y]["end"] and not maze[x, y]["start"] and not maze[x, y]["enemy"]:
                        random_item_amount = random.randint(1, 20)
                        if random_item_amount == 1:
                            self.pen.goto(x * self.size + offset_x, y * self.size + offset_y)
                            if self.chest_exists:
                                self.pen.shape("pictures/chest.gif")
                                maze[x,y]["id"] = self.pen.stamp()
                            else:
                                self.pen.color("lightgreen")
                                self.pen.stamp()
                            maze[x,y]["item"] = True

    def image(self):
        image = Image.open("pictures/background.png")
        image = image.resize((self.width, self.height))
        self.bg_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="center")

    def start_position(self):
        return self.start
