import json
import matplotlib.pyplot as plt
from lines import task1
from circles import task2
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

lines_img = json.load(open('image_hough.json', 'r'))
circles_img = json.load(open('image_circles.json', 'r'))

hough_space_lines = task1(lines_img)
hough_space_circles = np.array(task2(circles_img))
figure = plt.figure(figsize=(8,4))
figure.add_subplot(1, 2, 1)
plt.imshow(hough_space_lines)
plt.title('Hough space for lines json')
ax = figure.add_subplot(1, 2, 2, projection='3d')
x = np.arange(hough_space_circles.shape[0])[:hough_space_circles.shape[0] // 4, None, None]
y = np.arange(hough_space_circles.shape[1])[None, :hough_space_circles.shape[1] // 4, None]
z = np.arange(hough_space_circles.shape[2])[None, None, :hough_space_circles.shape[2] // 4]
x, y, z = np.broadcast_arrays(x, y, z)
ax.scatter(x.ravel(), y.ravel(), z.ravel())
plt.title('Hough space for circles json')
plt.show()