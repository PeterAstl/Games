
from turtle import RawTurtle
import random

class Player(RawTurtle):
    def __init__(self, screen_obj, maze, position):
        super().__init__(screen_obj.screen)
        self.penup()
        self.shape("square")
        self.color("violet")
        self.maze = maze
        self.screen_obj = screen_obj
        self.shapesize(self.screen_obj.size/20)
        self.hideturtle()
        self.goto(position)
        self.showturtle()
        self.current_start = None
        self.movement_enabled = True
        self.movement()
        self.direction = ""
        self.hp = 30
        self.weapon = False

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
            if self.weapon:
                self.hp -= random.randint(1, 2)
                print(f"You got {self.hp} ♥️")
            else:
                self.hp -= random.randint(1, 5)
                print(f"You got {self.hp} ♥️")
            if self.hp <= 0:
                print("️☠️game over☠️")
                self.movement_enabled = False
            random_hp_enemy = random.randint(1,2)
            if random_hp_enemy == 1:
                self.maze.maze[next_cell]["enemy"] = False
                print("Enemy Defeated")
            else:
                print("Enemy Still Alive")
        #ITEMS
        if self.maze.maze.get(next_cell)["item"]:
            self.maze.maze[next_cell]["item"] = False
            items = (self.damage,self.heal,self.sword)
            action = random.choice(items)
            action()


#ITEM EFFECTS#
    def damage(self):
        self.hp -= random.randint(1,2)
        print(f"ITS A MIMIC\n You got {self.hp} ♥️")
        if self.hp <= 0:
            print("️☠️game over☠️")
            self.movement_enabled = False

    def heal(self):
        heal_amount = random.randint(2,10)
        self.hp += heal_amount
        print(f"Its an +{heal_amount} Heal-Potion \n You got {self.hp} ♥️")

    def sword(self):
        self.weapon = True
        print("⚔️")
#ITEM EFFECTS#
