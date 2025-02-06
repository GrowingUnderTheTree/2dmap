import numpy as np
import pygame
import mainfile as mf
import random as r

perlin = mf.crazy(4,6,8,7)
val = np.array(perlin)
pygame.init()
TILE_SIZE = 10
GRID_SIZE = val.shape[0]
WIDTH, HEIGHT = GRID_SIZE * TILE_SIZE, GRID_SIZE * TILE_SIZE

def get_terrain_color(value):
    """Map height values to terrain colors."""
    if value < 0:   # Deepwater
        return (0, 0, 150)
    elif value < 0.05: #Water
        return (31, 106, 128)
    elif value < 0.06: #Shallow water
        return (129, 187, 204)
    elif value < 0.18: # Beach
        return (212, 196, 142)
    elif value < 0.2:  # Grass
        return (62, 176, 102)
    elif value < 0.4:  # Dirt
        return (156, 133, 53)
    else:              # Mountain
        return (49, 52, 54)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PERLIN NOISE")

for y in range(GRID_SIZE):
    for x in range(GRID_SIZE):
        RAND = r.uniform(0.95,1)
        color = get_terrain_color(val[y, x])
        newcolor = np.array(color) * RAND
        pygame.draw.rect(screen, newcolor, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.image.save(screen,'surface.png')
pygame.quit()