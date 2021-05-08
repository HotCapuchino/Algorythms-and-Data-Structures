import math


class Triangulator:

    def __init__(self):
        return

    def calculateSatelliteLocation(self, center_x, center_y, radius, angular_velocity, time):
        return \
            [center_x + radius * math.sin(angular_velocity * time),
             center_y + radius * math.cos(angular_velocity * time)]

    def calculateReceiverLocation(self, satellites):
        if len(satellites) < 3:
            print('Triangulation is impossible!')
            return
        x_s = []
        y_s = []
        radiuses = []
        for sat_option in satellites:
            x_s.append(sat_option.get('x'))
            y_s.append(sat_option.get('y'))
            radiuses.append(sat_option.get('radius'))
        receiver_x = ((y_s[1] - y_s[0]) *
                      (radiuses[1] ** 2 - radiuses[2] ** 2 - y_s[1] ** 2 + y_s[2] ** 2 - x_s[1] ** 2 + x_s[2] ** 2) -
                      (y_s[2] - y_s[1]) *
                      (radiuses[0] ** 2 - radiuses[1] ** 2 - y_s[0] ** 2 + y_s[1] ** 2 - x_s[0] ** 2 + x_s[1] ** 2)) / (2 * ((y_s[2] - y_s[1]) * (x_s[0] - x_s[1] ) - (y_s[1] - y_s[0]) * (x_s[1] - x_s[2])))
        receiver_y = ((x_s[1] - x_s[0]) *
                      (radiuses[1] ** 2 - radiuses[2] ** 2 - x_s[1] ** 2 + x_s[2] ** 2 - y_s[1] ** 2 + y_s[2] ** 2) -
                      (x_s[2] - x_s[1]) *
                      (radiuses[0] ** 2 - radiuses[1] ** 2 - x_s[0] ** 2 + x_s[1] ** 2 - y_s[0] ** 2 + y_s[1] ** 2)) / (2 * ((x_s[2] - x_s[1]) * (y_s[0] - y_s[1] ) - (x_s[1] - x_s[0]) * (y_s[1] - y_s[2])))
        return [receiver_x, receiver_y]