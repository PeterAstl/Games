
import tkinter as tk

class Gui:
    def __init__(self, maze_screen,maze):
        self.screen = maze_screen
        self.maze = maze
        self.level_text = tk.Label(self.screen.root, text="Level 1", font=("Arial",20), bg="grey",fg="white")
        self.level_text.place(anchor="center", x= self.screen.width/2, y = 50)
        self.hp_gui = tk.Label(self.screen.root, text="30♥️/30♥️", font=("Arial",20), bg="red", fg="black")
        self.hp_gui.place(anchor="center", x= 150, y= 50)
        self.text_log_text = tk.Label(self.screen.root, text="Welcome to the Maze", font=("Arial",15), bg="grey",fg="white")
        self.text_log_text.place(anchor="center", x= 150, y= self.screen.height - 50)
        self.xp_text = tk.Label(self.screen.root, text="XP: 0/10", font=("Arial", 20), bg="lightblue", fg="white")
        self.xp_text.place(anchor="center", x=self.screen.width - 100, y=50)
        self.game_over_text = False


    def hp_change(self, current_hp, max_hp, amount):
        self.hp_gui.configure(text=f"{current_hp}♥️/{max_hp}♥️")

    def level(self, level):
        self.level_text.configure(text=f"Level {level}")

    def text_log(self, text):
        self.text_log_text.configure(text=text)

    def game_over(self):
        self.game_over_text = tk.Label(self.screen.root, text="☠️GAME OVER☠️", font=("Arial", 80), bg="grey", fg="white")
        self.game_over_text.place(anchor="center", x=self.screen.width / 2, y=self.screen.height / 2)

    def xp(self, xp,xp_for_level_up):
        self.xp_text.configure(text=f"XP: {xp}/{xp_for_level_up}")
