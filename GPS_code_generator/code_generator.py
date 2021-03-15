import os


def generateG1RowCode():
    global G1_row
    new_bit = G1_row[2] ^ G1_row[9]
    G1_row = [new_bit] + G1_row[:9]
    return G1_row[9]


def generateG2RowCode():
    global G2_row
    new_bit = (G2_row[5] ^ G2_row[7] ^ G2_row[8] ^ G2_row[9]) ^ (G2_row[1] ^ G2_row[2])
    returned_bit = G2_row[G2_taps.get(satellite_number)[0] - 1] ^ G2_row[G2_taps.get(satellite_number)[1] - 1]
    G2_row = [new_bit] + G2_row[:9]
    return returned_bit


def generateNewCode():
    global new_code
    new_code.append(generateG1RowCode() ^ generateG2RowCode())


def readSatellitesOptions():
    global G2_taps
    with open('res/G2_taps.txt') as f:
        while True:
            string = f.readline()[:-1]
            if not string:
                break
            satellite_number, trash = string.split(' ')
            valueble_bits = list(map(int, trash.split('_')))
            G2_taps.update({int(satellite_number): valueble_bits})
    f.close()


def writeSatelliteCode():
    if not os.path.exists('out'):
        os.makedirs('out')
    with open('out/' + str(satellite_number) + '.txt', 'w') as f:
        for bit in new_code:
            f.write(str(bit))
    f.close()


G2_taps = dict()
try:
    readSatellitesOptions()
except Exception:
    print('Возникла ошибка при попытке прочтения файла!')
    exit(-1)
new_code = []
satellite_number = int(input('Введите номер спутника: (num > 1 && num < 32)\n'))
if satellite_number > 32 or satellite_number < 1:
    print('Некорректный номер спутника!')
    exit(-1)
if os.path.isfile('out/satellite' + str(satellite_number) + '.txt'):
    print('Для этого спутника уже была рассчитана битовая последовательность, нет нужды тратить время)')
    exit(0)
initial_vector = [1] * 10
G1_row = [1] * 10
G2_row = [1] * 10
while True:
    generateNewCode()
    if G1_row == initial_vector and G2_row == initial_vector:
        break
writeSatelliteCode()
