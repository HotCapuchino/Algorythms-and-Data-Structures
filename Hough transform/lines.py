import math


def task1(image):
    height, width = len(image), len(image[0])
    max_diag = round(math.sqrt(width ** 2 + height ** 2))
    phase_space = [[0 for i in range(max_diag)] for j in range(180)]
    for row in range(height):
        for col in range(width):
            if image[row][col]:
                for f in range(180):
                    theta = f * math.pi / 180
                    p = int((row - height / 2) * math.sin(theta) + (col - width / 2) * math.cos(theta))
                    phase_space[f][p] += 1
    return phase_space
