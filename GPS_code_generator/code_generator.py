import os
import pathlib
import random


class CodeGenerator:

    __G1_row = [1] * 10
    __G2_row = [1] * 10
    __G2_taps = dict()
    __satellite_number = None
    __generated_code = []
    __received_code = []

    def __init__(self, sat_number):
        if not self.__checkIfSatelliteExists(sat_number):
            raise Exception('Incorrect Satellite Number!')
        self.__satellite_number = sat_number
        if not self.__readSatellitesOptions():
            raise Exception('Unable to open file!')
        self.__generateCodesForAllSatellites()

    def __checkIfSatelliteExists(self, number):
        return not(number > 32 or number < 1)

    def __generateG1RowCode(self):
        new_bit = self.__G1_row[2] ^ self.__G1_row[9]
        self.__G1_row = [new_bit] + self.__G1_row[:9]
        return self.__G1_row[9]

    def __generateG2RowCode(self, number=None):
        sat_number = self.__satellite_number if not number else number
        new_bit = (self.__G2_row[5] ^ self.__G2_row[7] ^ self.__G2_row[8] ^ self.__G2_row[9]) ^ (self.__G2_row[1] ^ self.__G2_row[2])
        returned_bit = self.__G2_row[self.__G2_taps.get(sat_number)[0] - 1] ^ self.__G2_row[self.__G2_taps.get(sat_number)[1] - 1]
        self.__G2_row = [new_bit] + self.__G2_row[:9]
        return returned_bit

    def __generateNAVInfo(self):
        nav = []
        for i in range(128):
            nav.append(round(random.random()))
        return nav

    def generateCA(self):
        initial_vector = [1] * 10
        while True:
            self.__generated_code.append(self.__generateG1RowCode() ^ self.__generateG2RowCode())
            if self.__G1_row == initial_vector and self.__G2_row == initial_vector:
                break
        gen_file = open('./generated/gen.txt', 'w')
        res_str = ('').join(map(str, self.__generated_code))
        if not os.path.exists('./generated/' + self.__satellite_number + '.txt'):
            sat_file = open('./generated/' + self.__satellite_number + '.txt', 'w')
            sat_file.write(res_str)
        gen_file.write(res_str)
        self.__generateReceivedCode()
        gen_file.close()

    def __generateReceivedCode(self):
        rec_file = open('./received/rec.txt', 'w')
        n_cycles = random.randint(5, 12)
        rec_file.write(str(n_cycles) + '\n')
        for i in range(n_cycles):
            offset = random.randint(1, 1022)
            self.__received_code = self.__generated_code + self.__generateNAVInfo()
            offset_arr = self.__received_code[:offset]
            self.__received_code = self.__received_code[offset:]
            self.__received_code += offset_arr
            rec_file.write(('').join(map(str, self.__received_code)) + '\n')
        rec_file.close()


    def __readSatellitesOptions(self):
        with open('./res/G2_taps.txt', 'r') as f:
            while True:
                string = f.readline()[:-1]
                if not string:
                    break
                sat_number, trash = string.split(' ')
                valuable_bits = list(map(int, trash.split('_')))
                self.__G2_taps.update({int(sat_number): valuable_bits})
        return True

    def __generateCodesForAllSatellites(self):
        for i in range(1, 33, 1):
            if os.path.exists('./generated/' + str(i) + '.txt'):
                continue
            signal = open('./generated/' + str(i) + '.txt', 'w+')
            code = []
            initial_vector = [1] * 10
            while True:
                code.append(self.__generateG1RowCode() ^ self.__generateG2RowCode())
                if self.__G1_row == initial_vector and self.__G2_row == initial_vector:
                    break
            signal.write((''.join(map(str, code))))
            signal.close()
