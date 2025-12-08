
from mazebrain import *

maze = Maze(height=13, width=13)

maze.mix()
maze.draw()
player = Player(maze.screen, maze, maze.screen.start_position())
maze.screen.root.mainloop()