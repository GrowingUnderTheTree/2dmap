import cv2
import matplotlib.pyplot as plt
import numpy as np

def hmap():
    image = cv2.imread('surface.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    heightmap = np.mean(image, axis=2)  # Average RGB values for brightness
    heightmap = heightmap / 255.0 * 10  # Scale to height range 0-10
    return heightmap

img = hmap()
plt.imsave('heightmap.png',img)