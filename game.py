import numpy as np
import pygame
import mainfile as mf

perlin = mf.crazy(4,6,8,7)
val = np.array(perlin)
pygame.init()
TILE_SIZE = 10
GRID_SIZE = val.shape[0]
WIDTH, HEIGHT = GRID_SIZE * TILE_SIZE, GRID_SIZE * TILE_SIZE

def get_terrain_color(value):
    """Map height values to terrain colors."""
    if value < 0:   # Water
        return (0, 0, 150)
    elif value < 0.15: # beach
        return (240, 213, 93)
    elif value < 0.2:  # Grass
        return (34, 139, 34)
    elif value < 0.4:  # Dirt
        return (139, 69, 19)
    else:              # Mountain
        return (169, 169, 169)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PERLIN NOISE")

for y in range(GRID_SIZE):
    for x in range(GRID_SIZE):
        color = get_terrain_color(val[y, x])
        pygame.draw.rect(screen, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.image.save(screen,'surface.png')
pygame.quit()