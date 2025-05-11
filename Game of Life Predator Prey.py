
import pygame
import random

# Розміри вікна
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 10
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Кольори
EMPTY = (255, 255, 255)
PREY = (0, 255, 0)
PREDATOR = (255, 0, 0)

# Типи клітин
EMPTY_CELL = 0
PREY_CELL = 1
PREDATOR_CELL = 2

# Ініціалізація гри
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Predator-Prey Cellular Automata")
clock = pygame.time.Clock()

# Створення сітки
def create_grid():
    return [[random.choice([EMPTY_CELL, PREY_CELL, PREDATOR_CELL]) if random.random() < 0.1 else EMPTY_CELL for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Оновлення сітки
def update_grid(grid):
    new_grid = [[EMPTY_CELL for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            cell = grid[y][x]
            neighbors = get_neighbors(grid, x, y)
            if cell == PREY_CELL:
                if neighbors.count(PREDATOR_CELL) >= 1:
                    new_grid[y][x] = EMPTY_CELL  # З'їдено
                else:
                    new_grid[y][x] = PREY_CELL
            elif cell == PREDATOR_CELL:
                if neighbors.count(PREY_CELL) == 0:
                    new_grid[y][x] = EMPTY_CELL  # Помер від голоду
                else:
                    new_grid[y][x] = PREDATOR_CELL
            elif cell == EMPTY_CELL:
                if neighbors.count(PREY_CELL) >= 3:
                    new_grid[y][x] = PREY_CELL
                elif neighbors.count(PREDATOR_CELL) >= 2:
                    new_grid[y][x] = PREDATOR_CELL
    return new_grid

# Отримання сусідів
def get_neighbors(grid, x, y):
    neighbors = []
    for j in range(-1, 2):
        for i in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx, ny = (x + i) % GRID_WIDTH, (y + j) % GRID_HEIGHT
            neighbors.append(grid[ny][nx])
    return neighbors

# Малювання сітки
def draw_grid(grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            color = EMPTY
            if grid[y][x] == PREY_CELL:
                color = PREY
            elif grid[y][x] == PREDATOR_CELL:
                color = PREDATOR
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Основний цикл
def main():
    grid = create_grid()
    running = True
    while running:
        screen.fill(EMPTY)
        draw_grid(grid)
        pygame.display.flip()
        grid = update_grid(grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(5)
    pygame.quit()

if __name__ == "__main__":
    main()
