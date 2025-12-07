
from turtle import RawTurtle


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

    def move_right(self):
        if self.movement_enabled:
            cells = self.offset()
            next_cell = (cells[0] + 1, cells[1])
            if not self.maze.maze.get(next_cell)["wall"]:
                self.goto(self.xcor() + self.screen_obj.size, self.ycor())
            if self.maze.maze.get(next_cell)["end"]:
                self.reset_maze()

    def move_left(self):
        if self.movement_enabled:
            cells = self.offset()
            next_cell = (cells[0] - 1, cells[1])
            if not self.maze.maze.get(next_cell)["wall"]:
                self.goto(self.xcor() - self.screen_obj.size, self.ycor())
            if self.maze.maze.get(next_cell)["end"]:
                self.reset_maze()

    def move_down(self):
        if self.movement_enabled:
            cells = self.offset()
            next_cell = (cells[0], cells[1] - 1)
            if not self.maze.maze.get(next_cell)["wall"]:
                self.goto(self.xcor(), self.ycor() - self.screen_obj.size)
            if self.maze.maze.get(next_cell)["end"]:
                self.reset_maze()

    def move_up(self):
        if self.movement_enabled:
            cells = self.offset()
            next_cell = (cells[0], cells[1] + 1)
            if not self.maze.maze.get(next_cell)["wall"]:
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
        self.goto(new_x + self.maze.screen.size, new_y + self.maze.screen.size)
        self.movement_enabled = True
        self.showturtle()

