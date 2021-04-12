import random
import time
from matplotlib import pyplot as plt


class AlgoTester:

    def __init__(self):
        self.test_array = None
        self.results = None

    def setTestArray(self, input_array):
        self.test_array = input_array

    def __testAlgo(self, input_array, expected_array, sorting_function):
        if sorting_function(input_array) == expected_array:
            return True
        return False

    def calculateTime(self, sorting_function, iterations=3, start_amount=100, epochs=5):
        self.results = dict()
        for i in range(start_amount, start_amount * epochs + 1, start_amount):
            for j in range(iterations):
                test_array = []
                for k in range(i):
                    test_array.append(random.randint(0, 100))
                start_time = time.time()
                result = self.__testAlgo(test_array, sorted(test_array), sorting_function)
                if result:
                    end_time = time.time()
                    if i in self.results.keys():
                        list = self.results.get(i)
                        list.append(end_time - start_time)
                        self.results.update({i: list})
                    else:
                        self.results.update({i: [end_time - start_time]})

    def drawGraphics(self, name):
        x = self.results.keys()
        y = []
        for key in x:
            sum = 0
            list = self.results.get(key)
            for i in range(len(list)):
                sum += list[i]
            y.append(sum / len(list))
        plt.plot(y)
        plt.xticks(range(len(x)), x)
        plt.title(name)
        plt.ylabel('Time in ms')
        plt.xlabel('Amount of array')
        plt.fill_between(range(len(x)), y, alpha=0.4)
        plt.show()
