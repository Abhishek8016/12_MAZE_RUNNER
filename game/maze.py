import pygame
import random

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False

    def draw(self, surface, cell_size):
        x = self.x * cell_size
        y = self.y * cell_size
        color = (255, 255, 255)
        thickness = 2

        if self.walls['top']:
            pygame.draw.line(surface, color, (x, y), (x + cell_size, y), thickness)
        if self.walls['right']:
            pygame.draw.line(surface, color, (x + cell_size, y), (x + cell_size, y + cell_size), thickness)
        if self.walls['bottom']:
            pygame.draw.line(surface, color, (x + cell_size, y + cell_size), (x, y + cell_size), thickness)
        if self.walls['left']:
            pygame.draw.line(surface, color, (x, y + cell_size), (x, y), thickness)


class Maze:
    def __init__(self, cols, rows, cell_size):
        self.cols = cols
        self.rows = rows
        self.cell_size = cell_size
        self.grid = [[Cell(x, y) for x in range(cols)] for y in range(rows)]
        self.generate_maze()

    def generate_maze(self):
        stack = []
        current = self.grid[0][0]
        current.visited = True

        while True:
            neighbors = self.get_unvisited_neighbors(current)
            if neighbors:
                next_cell, direction = random.choice(neighbors)
                self.remove_walls(current, next_cell, direction)
                stack.append(current)
                current = next_cell
                current.visited = True
            elif stack:
                current = stack.pop()
            else:
                break

    def get_unvisited_neighbors(self, cell):
        neighbors = []
        x, y = cell.x, cell.y

        if y > 0 and not self.grid[y - 1][x].visited:
            neighbors.append((self.grid[y - 1][x], 'top'))
        if x < self.cols - 1 and not self.grid[y][x + 1].visited:
            neighbors.append((self.grid[y][x + 1], 'right'))
        if y < self.rows - 1 and not self.grid[y + 1][x].visited:
            neighbors.append((self.grid[y + 1][x], 'bottom'))
        if x > 0 and not self.grid[y][x - 1].visited:
            neighbors.append((self.grid[y][x - 1], 'left'))

        return neighbors

    def remove_walls(self, current, next_cell, direction):
        if direction == 'top':
            current.walls['top'] = False
            next_cell.walls['bottom'] = False
        elif direction == 'right':
            current.walls['right'] = False
            next_cell.walls['left'] = False
        elif direction == 'bottom':
            current.walls['bottom'] = False
            next_cell.walls['top'] = False
        elif direction == 'left':
            current.walls['left'] = False
            next_cell.walls['right'] = False

    def draw(self, surface):
        for row in self.grid:
            for cell in row:
                cell.draw(surface, self.cell_size)