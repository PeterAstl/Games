import os
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
import time
import random

def choice_1():
    text = entry.get()
    if text in class_list:
        classes_choose.destroy()
        classes.destroy()
        entry.destroy()
        choice.destroy()
        window.config(bg="green")
        for pic in os.listdir(text):
                img_list.append(pic)

        print(img_list)
        start(img_list, text, False)
    else:
        window.config(bg="red")
        window.update()
        time.sleep(2)
        window.config(bg="blue")

window = Tk()
window.title("Smash or Pass",)
window.geometry("1920x1080")
window.config(bg="blue")
style = ttk.Style()
style.theme_use("clam")   # sieht moderner aus
z = 0
y = -1

style.configure(
    "My.TButton",
    font=("Segoe UI", 14),
    padding=10,
    background="#222",
    foreground="white"
)

for i in range(5):
    window.grid_rowconfigure(i, weight=1)

for i in range(3):
    window.grid_columnconfigure(i, weight=1)

title_label = ttk.Label(window, text="Smash or Pass", style="My.TButton")
title_label.grid(column=1, row=0)

img_list = []
class_list = ["Normal","Cursed", "Things"]

classes_choose = ttk.Label(window, text=f"Classes to Choose from", style="My.TButton")
classes_choose.grid(column=1, row=1)
classes = ttk.Label(window, text=f"{class_list}", style="My.TButton")
classes.grid(column=1, row=2)

entry = ttk.Entry(window, width=30, style="My.TButton")
entry.grid(column=1, row=3)
choice = ttk.Button(window, text="Yes that one", style="My.TButton", command = choice_1)
choice.grid(column=1, row=4)

starting = True

def start(img_list, text, type):
    global z
    if type:
        z = z + 1
    global starting
    global y
    y = y + 1
    if starting:
        if len(img_list) != 0:
            button_smash = ttk.Button(window, text="Smash", style="My.TButton", command = lambda:(start(img_list,text,True)))
            button_smash.grid(column=0, row=3)
            button_pass = ttk.Button(window, text="Pass",style="My.TButton", command = lambda:(start(img_list,text, False)))
            button_pass.grid(column=2, row=3)
            x = random.choice(img_list)
            pil_img = Image.open(f"./{text}/{x}")
            pil_img = pil_img.resize((500, 500))
            random_image = ImageTk.PhotoImage(pil_img)
            canvas = Canvas(width=500, height=500, bg="Green", highlightthickness=0)
            canvas.image = random_image
            canvas.create_image(100, 100, image=random_image)
            canvas.grid(row=2, column=1)
            canvas.update()
            x = img_list.remove(x)
            starting = False
        else:
            print(f"{z}/{y}")
            window.destroy()
    else:
        if len(img_list) != 0:
            x = random.choice(img_list)
            pil_img = Image.open(f"./{text}/{x}")
            pil_img = pil_img.resize((800, 800))
            random_image = ImageTk.PhotoImage(pil_img)
            canvas = Canvas(width=500, height=500, bg="Green", highlightthickness=0)
            canvas.image = random_image
            canvas.create_image(100, 100, image=random_image)
            canvas.grid(row=2, column=1)
            canvas.update()
            x = img_list.remove(x)
        else:
            print(f"{z}/{y}")
            window.destroy()

window.mainloop()