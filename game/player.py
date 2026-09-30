import pygame

class Player:
    def __init__(self, x, y, cell_size):
        self.grid_x = x
        self.grid_y = y
        self.cell_size = cell_size

    def move(self, dx, dy, maze):
        """
        Moves the player in grid coordinates (dx, dy) only if 
        there is no wall blocking the path in the maze.
        """
        current_cell = maze.grid[self.grid_y][self.grid_x]
        
        # Check Direction and Wall status before moving
        if dx == 0 and dy == -1: # Move Up
            if not current_cell.walls['top']:
                self.grid_y += dy
        elif dx == 0 and dy == 1: # Move Down
            if not current_cell.walls['bottom']:
                self.grid_y += dy
        elif dx == -1 and dy == 0: # Move Left
            if not current_cell.walls['left']:
                self.grid_x += dx
        elif dx == 1 and dy == 0: # Move Right
            if not current_cell.walls['right']:
                self.grid_x += dx

    def draw(self, surface):
        """Draws the ball centered inside the current maze cell."""
        center_x = self.grid_x * self.cell_size + self.cell_size // 2
        center_y = self.grid_y * self.cell_size + self.cell_size // 2
        radius = self.cell_size // 3
        
        # Draw player ball
        pygame.draw.circle(surface, (230, 50, 50), (center_x, center_y), radius)