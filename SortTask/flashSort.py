from testFunc import AlgoTester


def flash_sort(input_array):
    array_length = len(input_array)
    m = int(array_length * 0.42)
    sublist = [0] * m
    i, j, k = 0, 0, 0
    min_elem = input_array[0]
    max_elem_index = 0
    for i in range(1, array_length, 1):
        if input_array[i] < min_elem:
            min_elem = input_array[i]
        if input_array[i] > input_array[max_elem_index]:
            max_elem_index = i
    if min_elem == input_array[max_elem_index]:
        return
    c1 = (m - 1) / (input_array[max_elem_index] - min_elem)
    for i in range(array_length):
        k = int(c1 * (input_array[i] - min_elem))
        sublist[k] += 1
    for i in range(1, m, 1):
        sublist[i] += sublist[i - 1]
    input_array[max_elem_index], input_array[0] = input_array[0], input_array[max_elem_index]
    elems_moved = 0
    flash = None
    j = 0
    k = m - 1
    while elems_moved < array_length - 1:
        while j > (sublist[k] - 1):
            j += 1
            k = int(c1 * (input_array[j] - min_elem))
        flash = input_array[j]
        while not j == sublist[k]:
            k = int(c1 * (flash - min_elem))
            input_array[sublist[k] - 1], flash = flash, input_array[sublist[k] - 1]
            sublist[k] -= 1
            elems_moved += 1
    for i in range(len(input_array) - 3, -1, -1):
        if input_array[i + 1] < input_array[i]:
            buffer = input_array[i]
            j = i
            while input_array[j + 1] < buffer:
                input_array[j] = input_array[j + 1]
                j += 1
            input_array[j] = buffer
    return input_array


algoTester = AlgoTester()
algoTester.setTestArray([10, 29, 18, 2, 4, 91, 105, 0, 0, 101, -10])
algoTester.calculateTime(flash_sort, start_amount=1000, epochs=10)
algoTester.drawGraphics('FlashSort Algorythm')
