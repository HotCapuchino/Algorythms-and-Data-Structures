import matplotlib.pyplot as plt
import json
import math

cell_size = 10


def calculateParameters(cell1, cell2):
    # return a, b
    a = "empty"
    b = "empty"
    try:
        a = (cell1[0] - cell2[0]) / (cell1[1] - cell2[1])
        b = (cell2[0] * cell1[1] - cell1[0] * cell2[1]) / (cell1[1] - cell2[1])
    except ZeroDivisionError as err:
        err.with_traceback()
        # print("Division by zero!")
    finally:
        if type(a) != str and type(b) != str:
            return a, b
        else:
            return -1


with open('image_hough.json', 'r') as f:
    image = json.load(f)
    painted_dots = []
    line_parameters = []
    coeff_weights = []
    for y in range(len(image)):
        for x in range(len(image[y])):
            if image[y][x] != 0:
                painted_dots.append([y, x])
    for i in range(1, len(painted_dots)):
        for j in range(i, len(painted_dots), 1):
            result = calculateParameters(painted_dots[i], painted_dots[j])
            if type(result) != int:
                line_parameters.append(calculateParameters(painted_dots[i], painted_dots[j]))
    print(len(line_parameters))
    A_max = max(line_parameters[i][0] for i in range(len(line_parameters)))
    A_min = min(line_parameters[i][0] for i in range(len(line_parameters)))
    B_max = max(line_parameters[i][1] for i in range(len(line_parameters)))
    B_min = min(line_parameters[i][1] for i in range(len(line_parameters)))
    print(A_max, A_min, B_max, B_min)
    for i in range(math.floor(A_max - A_min)):
        coeff_weights.append([0] * math.floor(B_max - B_min))
    for line_params in line_parameters:
        coeff_weights[math.floor((line_params[0] - A_min) / cell_size)][
            math.floor((line_params[1] - B_min) / cell_size)] += 1
    image = coeff_weights
plt.imshow(image)
plt.show()
