import pygame
import sys
from game.maze import Maze
from game.player import Player

class GameEngine:
    def __init__(self, cols=15, rows=12, cell_size=40):
        self.cols = cols
        self.rows = rows
        self.cell_size = cell_size
        self.width = cols * cell_size
        self.height = rows * cell_size

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Maze Runner")
        self.clock = pygame.time.Clock()

        self.reset_game()

    def reset_game(self):
        self.maze = Maze(self.cols, self.rows, self.cell_size)
        self.player = Player(0, 0, self.cell_size)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_UP):
                    self.player.move(0, -1, self.maze)
                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    self.player.move(0, 1, self.maze)
                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    self.player.move(-1, 0, self.maze)
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    self.player.move(1, 0, self.maze)
                elif event.key == pygame.K_r:
                    self.reset_game()

    def update(self):
        # Win condition check
        if self.player.grid_x == self.cols - 1 and self.player.grid_y == self.rows - 1:
            print("Maze Cleared!")

    def draw(self):
        self.screen.fill((20, 20, 20))
        
        # Draw exit target
        exit_rect = pygame.Rect(
            (self.cols - 1) * self.cell_size + 4,
            (self.rows - 1) * self.cell_size + 4,
            self.cell_size - 8,
            self.cell_size - 8
        )
        pygame.draw.rect(self.screen, (50, 200, 50), exit_rect)

        self.maze.draw(self.screen)
        self.player.draw(self.screen)
        
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)