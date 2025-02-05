from perlin_noise import PerlinNoise
def crazy(o1,o2,o3,o4):
    noise1 = PerlinNoise(octaves=o1)
    noise2 = PerlinNoise(octaves=o2)
    noise3 = PerlinNoise(octaves=o3)
    noise4 = PerlinNoise(octaves=o4)

    xpix, ypix = 100, 100
    pic = []
    for i in range(xpix):
        row = []
        for j in range(ypix):
            noise_val = noise1([i / xpix, j / ypix])
            noise_val += 0.5 * noise2([i / xpix, j / ypix])
            noise_val += 0.25 * noise3([i / xpix, j / ypix])
            noise_val += 0.125 * noise4([i / xpix, j / ypix])

            row.append(noise_val)
        pic.append(row)
    return pic