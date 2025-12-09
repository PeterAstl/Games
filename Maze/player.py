
from turtle import RawTurtle
import random
from PIL import Image
import os

class Player(RawTurtle):
    def __init__(self, screen_obj, maze, position, gui):
        super().__init__(screen_obj.screen)
        self.penup()
        self.maze = maze
        self.screen_obj = screen_obj
        if os.path.exists("pictures/Son_Goku.png"):
            img = Image.open("pictures/Son_Goku.png")
            img = img.resize((self.screen_obj.size, self.screen_obj.size))
            img.save("pictures/Son_Goku.gif")
            self.screen_obj.screen.addshape("pictures/Son_Goku.gif")
            self.shape("pictures/Son_Goku.gif")
        else:
            self.shape("Square")
        self.shapesize(self.screen_obj.size/20)
        self.hideturtle()
        self.goto(position)
        self.showturtle()
        self.current_start = None
        self.movement_enabled = True
        self.movement()
        self.gui = gui
        self.direction = ""
        self.max_hp = 30
        self.current_hp = 30
        self.weapon_level = 0
        self.weapon_dmg = 0
        self.weapons = {"Common Stick": 1,
                        "Uncommon Club": 2,
                        "Rare Axe": 3,
                        "Epic Sword": 4,
                        "Legendary Scythe": 5,
                        "Divine Dual Blades": 7,
                        }
        self.level_amount = 1
        self.xp = 0
        self.xp_for_level_up = 10



    def move_right(self):
        if self.movement_enabled:
            self.direction = "right"
            cells = self.offset()
            next_cell = (cells[0] + 1, cells[1])
            if not self.maze.maze.get(next_cell)["wall"] and not self.maze.maze.get(next_cell)["enemy"] and not self.maze.maze.get(next_cell)["item"]:
                self.goto(self.xcor() + self.screen_obj.size, self.ycor())
            if self.maze.maze.get(next_cell)["end"]:
                self.reset_maze()

    def move_left(self):
        if self.movement_enabled:
            self.direction = "left"
            cells = self.offset()
            next_cell = (cells[0] - 1, cells[1])
            if not self.maze.maze.get(next_cell)["wall"] and not self.maze.maze.get(next_cell)["enemy"] and not self.maze.maze.get(next_cell)["item"]:
                self.goto(self.xcor() - self.screen_obj.size, self.ycor())
            if self.maze.maze.get(next_cell)["end"]:
                self.reset_maze()

    def move_down(self):
        if self.movement_enabled:
            self.direction = "down"
            cells = self.offset()
            next_cell = (cells[0], cells[1] - 1)
            if not self.maze.maze.get(next_cell)["wall"] and not self.maze.maze.get(next_cell)["enemy"] and not self.maze.maze.get(next_cell)["item"]:
                self.goto(self.xcor(), self.ycor() - self.screen_obj.size)
            if self.maze.maze.get(next_cell)["end"]:
                self.reset_maze()

    def move_up(self):
        if self.movement_enabled:
            self.direction = "up"
            cells = self.offset()
            next_cell = (cells[0], cells[1] + 1)
            if not self.maze.maze.get(next_cell)["wall"] and not self.maze.maze.get(next_cell)["enemy"] and not self.maze.maze.get(next_cell)["item"]:
                self.goto(self.xcor(), self.ycor() + self.screen_obj.size)
            if self.maze.maze.get(next_cell)["end"]:
                self.reset_maze()

    def offset(self):
        cell_x = round((self.xcor() + (self.maze.width * self.screen_obj.size /2)) / self.screen_obj.size)
        cell_y = round((self.ycor() + (self.maze.height * self.screen_obj.size /2)) / self.screen_obj.size)
        return cell_x,cell_y

    def movement(self):
        self.screen.listen()
        self.screen.onkey(self.move_up, "w")
        self.screen.onkey(self.move_down, "s")
        self.screen.onkey(self.move_left, "a")
        self.screen.onkey(self.move_right, "d")
        self.screen.onkey(self.interact, "e")

    def reset_maze(self):
        self.movement_enabled = False
        self.hideturtle()
        self.maze.maze_clear()
        for (x, y), cell in self.maze.maze.items():
            if cell["start"]:
                self.current_start = (x, y)
                break
        new_x = self.current_start[0] - self.maze.width * self.screen_obj.size /2
        new_y = self.current_start[1] - self.maze.height * self.screen_obj.size /2
        self.goto(new_x + self.maze.screen.size -1, new_y + self.maze.screen.size -1)
        self.movement_enabled = True
        self.showturtle()
        self.level_amount +=1
        self.gui.level(self.level_amount)

    def interact(self):
        if self.movement_enabled:
            if self.direction == "right":
                # print("right")
                self.interactable_obj(1,0)
            if self.direction == "left":
                # print("left")
                self.interactable_obj(-1, 0)
            if self.direction == "down":
                # print("down")
                self.interactable_obj(0, -1)
            if self.direction == "up":
                # print("up")
                self.interactable_obj(0, 1)

    def interactable_obj(self, x, y):
        cells = self.offset()
        next_cell = (cells[0] + x, cells[1] + y)
        #ENEMY
        if self.maze.maze.get(next_cell)["enemy"]:
            dmg_amount = random.randint(1, 3)
            self.current_hp -= dmg_amount
            self.gui.text_log(f"You got {dmg_amount} Dmg!")
            self.gui.hp_change(self.current_hp, self.max_hp, dmg_amount)
            if self.current_hp <= 0:
                self.gui.game_over()
                self.movement_enabled = False
            random_hp_enemy = random.randint(1,max(self.level_amount-self.weapon_dmg, 1))
            if random_hp_enemy == 1:
                self.maze.maze[next_cell]["enemy"] = False
                self.gui.text_log(f"You defeated the Monster \n It dealt {dmg_amount} Dmg!")
                self.xp += 1
                self.gui.xp(self.xp, self.xp_for_level_up)
                self.screen_obj.pen.clearstamp(self.maze.maze[next_cell]["id"])
                if self.xp >= self.xp_for_level_up:
                    self.xp = 0
                    self.xp_for_level_up += 5
                    self.current_hp += 3
                    self.gui.xp(self.xp, self.xp_for_level_up)
                    self.gui.text_log("You Leveled Up\n +3 HP for you!")
            else:
                self.gui.text_log(f"Its Still Alive \n It dealt {dmg_amount} Dmg!")

        #ITEMS
        if self.maze.maze.get(next_cell)["item"]:
            self.maze.maze[next_cell]["item"] = False
            items = (self.damage,self.heal,self.weapon_type, self.heal_upgrade)
            action = random.choice(items)
            action()
            self.screen_obj.pen.clearstamp(self.maze.maze[next_cell]["id"])


#ITEM EFFECTS#
    def damage(self):
        dmg_amount = random.randint(1, 2)
        self.current_hp -= dmg_amount
        self.gui.hp_change(self.current_hp,self.max_hp,dmg_amount)
        self.gui.text_log(f"☠️ ITS WAS A MIMIC ☠️\n It dealt {dmg_amount} Dmg")
        if self.current_hp <= 0:
            self.gui.game_over()
            self.movement_enabled = False

    def heal(self):
        heal_amount = random.randint(3,10)
        self.current_hp += heal_amount
        self.current_hp = min(self.current_hp, self.max_hp)
        self.gui.hp_change(self.current_hp, self.max_hp, heal_amount)
        self.gui.text_log(f"Its an Heal-Potion \n It healed you for {heal_amount} HP")

    def weapon_type(self):
        if self.weapon_level <= len(self.weapons) - 1:
            while True:
                random_upgrade = random.randint(1,max(2*self.weapon_level, 1))
                if random_upgrade == 1:
                    self.weapon_level = min(self.weapon_level, len(self.weapons) - 1)
                    items_list = list(self.weapons.items())
                    key, value = items_list[self.weapon_level]
                    self.weapon_dmg = value
                    self.gui.text_log(f"Its a new weapon: {key}")
                    self.gui.weapon_gui(key, value)
                    self.weapon_level += 1
                else:
                    break
        else:
            self.gui.text_log(f"You already got the strongest Weapon")

    def heal_upgrade(self):
        heal_amount = random.randint(1,3)
        self.max_hp += heal_amount
        self.gui.hp_change(self.current_hp, self.max_hp, heal_amount)
        self.gui.text_log(f"Its an Heal-Upgrade \n It increased ur Max HP by {heal_amount}!")

#ITEM EFFECTS#
