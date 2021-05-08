from code_generator import CodeGenerator
from correlator import Corellator
from triangular import Triangulator

# #task 1
code_generator = CodeGenerator(1)  # any number you want
# code_generator.generateCA()

# #task 2
code_corellator = Corellator()
signals_offsets = code_corellator.calculateOffsets()
for i in range(len(signals_offsets)):
    print(f'{i + 1} signal offset is {signals_offsets[i]}')

# task 3
print(code_corellator.findPRN())

# task 4
triangulator = Triangulator()
print('Satellite location: ' + str(triangulator.calculateSatelliteLocation(300, 1000, 4000, 50, 100)))

# task 5
satellites = [
    {
        'x': 1000,
        'y': 20000,
        'radius': 16000
    },
    {
        'x': 5000,
        'y': 13000,
        'radius': 25000
    },
    {
        'x': 10000,
        'y': 4000,
        'radius': 13000
    }
]
print('Receiver location: ' + str(triangulator.calculateReceiverLocation(satellites)))
