
class Corellator:

    __generated_code = []
    __received_codes = []
    __signal_offsets = []
    __existing_codes = []

    def __init__(self):
        self.__readGeneratedCode()
        self.__readReceivedCode()

    def __readExistingCodes(self):
        for i in range(1, 33, 1):
            signal = open('./generated/' + str(i) + '.txt', 'r')
            code = []
            data = signal.read()
            for char in data:
                code.append(int(char))
            self.__existing_codes.append(code)
            signal.close()

    def __readGeneratedCode(self):
        gen_file = open('./generated/gen.txt', 'r')
        data = gen_file.read()
        for char in data:
            self.__generated_code.append(int(char))
        gen_file.close()

    def __readReceivedCode(self):
        rec_file = open('./received/rec.txt', 'r')
        n_cycles = int(rec_file.readline()[:-1])
        for i in range(n_cycles):
            received = []
            rec_str = rec_file.readline()[:-1]
            # это делается для того, чтобы потом можно было двигаться и сравнивать принятый сигнал не волнуясь о сдвиге
            for i in range(2):
                for char in rec_str:
                    received.append(int(char))
            self.__received_codes.append(received)
        rec_file.close()

    def calculateOffsets(self):
        for rec_code in self.__received_codes:
            offset = 0
            for j in range(len(rec_code) - len(self.__generated_code) + 1):
                equals = True
                for k in range(len(self.__generated_code)):
                    if self.__generated_code[k] != rec_code[k + offset]:
                        offset += 1
                        equals = False
                        break
                if equals:
                    self.__signal_offsets.append(offset)
                    break
        return self.__signal_offsets

    def findPRN(self):
        if not len(self.__signal_offsets):
            print('First of all calculate signals offsets!')
            return
        self.__readExistingCodes()
        # lets take first signal and its offset to determine satellite prn
        received_code = self.__received_codes[0][self.__signal_offsets[0]:self.__signal_offsets[0] + 1023]
        satellite_number = None
        for i in range(len(self.__existing_codes)):
            code = self.__existing_codes[i]
            found = True
            for j in range(len(code)):
                if code[j] != received_code[j]:
                    found = False
                    break
            if found:
                satellite_number = i + 1
                break
        return satellite_number
