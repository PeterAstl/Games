from gui import Gui
from mazebrain import *

maze = Maze(height=13, width=13)

maze.mix()
maze.draw()
gui = Gui(maze.screen, maze)
player = Player(maze.screen, maze, maze.screen.start_position(),gui)
maze.screen.root.mainloop()