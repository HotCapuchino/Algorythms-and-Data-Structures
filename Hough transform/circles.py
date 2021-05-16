import math


def task2(image):
    height, width = len(image), len(image[0])
    max_radius = None
    if height > width:
        max_radius = width // 2
    else:
        max_radius = height // 2
    phase_space = [[[0 for i in range(max_radius)] for j in range(width)] for k in range(height)]
    for row in range(height):
        for col in range(width):
            if image[row][col]:
                for f in range(361):
                    theta = f * math.pi / 180
                    for r in range(max_radius):
                        a = int(row - r * math.sin(theta))
                        b = int(col - r * math.cos(theta))
                        if a <= row and b <= col:
                            phase_space[a][b][r] += 1
    return phase_space
