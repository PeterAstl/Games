
import tkinter as tk

class Gui:
    def __init__(self, maze_screen,maze):
        self.screen = maze_screen
        self.maze = maze
        self.level_text = tk.Label(self.screen.root, text="Level 1", font=("Consolas",20), bg="grey",fg="white", bd= 2, relief= "groove")
        self.level_text.place(anchor="center", x= self.screen.width/2, y = 50)
        self.hp_gui = tk.Label(self.screen.root, text="30/30♥", font=("Consolas",20), bg="red", fg="black", bd= 2, relief= "groove")
        self.hp_gui.place(anchor="center", x= 150, y= 50)
        self.text_log_text = tk.Label(self.screen.root, text="Welcome to the Maze", font=("Consolas",15), bg="grey",fg="white", bd= 2, relief= "groove")
        self.text_log_text.place(anchor="center", x= self.screen.width/2, y= self.screen.height - 100)
        self.xp_text = tk.Label(self.screen.root, text="XP: 0/10", font=("Consolas", 20), bg="#14A6E0", fg="white", bd= 2, relief= "groove")
        self.xp_text.place(anchor="center", x=self.screen.width - 100, y=50)
        self.weapon_text = tk.Label(self.screen.root, text="No Weapon", font=("Consolas", 20), bg="black", fg="white", bd= 2, relief= "groove")
        self.weapon_text.place(anchor="center", x=self.screen.width - 100, y=150)
        self.game_over_text = False
        self.highscore = 0
        with open("highscore.txt", "a") as file:
            file.write("")
        with open("highscore.txt", "r") as file:
            highscore_file_text = file.read()
        self.highscore_text = tk.Label(self.screen.root, text=highscore_file_text, font=("Consolas", 20), bg="#E0C453", fg="white", bd= 2, relief= "groove")
        self.highscore_text.place(anchor="center", x= self.screen.width/2, y = 100)


    def hp_change(self, current_hp, max_hp, amount):
        self.hp_gui.configure(text=f"{current_hp}/{max_hp}♥")

    def level(self, level):
        self.level_text.configure(text=f"Level {level}")
        self.highscore = level

    def text_log(self, text):
        self.text_log_text.configure(text=text)

    def game_over(self):
        self.game_over_text = tk.Label(self.screen.root, text="☠️GAME OVER☠️", font=("Consolas", 80), bg="grey", fg="white")
        self.game_over_text.place(anchor="center", x=self.screen.width / 2, y=self.screen.height / 2)
        with open("highscore.txt", "w") as file:
            file.write("Highscore: " + str(self.highscore))

    def xp(self, xp,xp_for_level_up):
        self.xp_text.configure(text=f"XP: {xp}/{xp_for_level_up}")

    def weapon_gui(self,text, value):
        if value == 1:
            color = "grey"
        elif value == 2:
            color = "green"
        elif value == 3:
            color = "blue"
        elif value == 4:
            color = "violet"
        elif value == 5:
            color = "yellow"
        elif value == 7:
            color = "red"
        else:
            color = "black"
        self.weapon_text.configure(text=text, fg=color)
