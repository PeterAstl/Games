
import tkinter as tk
import turtle
from PIL import ImageTk
from player import *

class Screen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Maze")
        self.root.geometry("800x800")
        self.width = 1900
        self.height = 1000

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("white")
        self.pen = turtle.RawTurtle(self.screen)
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed("fastest")
        self.size = 25
        self.pen.color("grey")
        self.pen.shape("square")
        self.pen.shapesize(self.size/20)
        self.start = [1,1]
        self.bg_image = ""
        self.image()
        pic_list = ("relaxo", "sand", "chest", "loch")
        self.icons = []

        for picture in pic_list:
            if os.path.exists(f"pictures/{picture}.png"):
                img = Image.open(f"pictures/{picture}.png")
                img = img.resize((self.size, self.size))
                img.save(f"pictures/{picture}.gif")
                self.screen.addshape(f"pictures/{picture}.gif")
                self.icons.append(picture)


    def paint(self, maze, height, width):
        offset_x = round(-width * self.size /2)
        offset_y = round(-height * self.size /2)
        for y in range(height):
            for x in range(width):
                if maze[x, y]["wall"]:
                    self.pen.goto(x * self.size + offset_x, y * self.size + offset_y)
                    if "sand" in self.icons:
                        self.pen.shape("pictures/sand.gif")
                        self.pen.stamp()
                        self.pen.shape("square")
                    else:
                        self.pen.color("grey")
                        self.pen.stamp()
                elif maze[x, y]["start"]:
                    self.start = [x * self.size + offset_x, y * self.size + offset_y]

                elif maze[x, y]["end"]:
                    self.pen.goto(x * self.size + offset_x, y * self.size + offset_y)
                    if "loch" in self.icons:
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
                            if "relaxo" in self.icons:
                                self.pen.shape("pictures/relaxo.gif")
                                maze[x,y]["id"] = self.pen.stamp()
                            else:
                                self.pen.color("red")
                                self.pen.stamp()
                            maze[x, y]["enemy"] = True
                    if not maze[x, y]["wall"] and not maze[x, y]["end"] and not maze[x, y]["start"] and not maze[x, y]["enemy"]:
                        random_item_amount = random.randint(1, 15)
                        if random_item_amount == 1:
                            self.pen.goto(x * self.size + offset_x, y * self.size + offset_y)
                            if "chest" in self.icons:
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
