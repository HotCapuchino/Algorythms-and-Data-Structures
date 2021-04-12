from testFunc import AlgoTester


def strand_sort(input_arr, descending_order=False):
    output_arr = []
    while len(input_arr):
        indexes_to_pop = []
        sublist = [input_arr[0]]
        indexes_to_pop.append(0)
        sublist_index = 0
        for i in range(1, len(input_arr), 1):
            if descending_order:
                if input_arr[i] < sublist[sublist_index]:
                    sublist.append(input_arr[i])
                    sublist_index += 1
                    indexes_to_pop.append(i)
            else:
                if input_arr[i] > sublist[sublist_index]:
                    sublist.append(input_arr[i])
                    sublist_index += 1
                    indexes_to_pop.append(i)
        for i in range(len(indexes_to_pop) - 1, -1, -1):
            input_arr.pop(indexes_to_pop[i])
        output_arr = merge(sublist, output_arr, descending_order)
    return output_arr


def merge(arr1, arr2, descending_order):
    united_array = []
    array1_index = 0
    array2_index = 0
    while True:
        if array1_index == len(arr1):
            united_array += arr2[array2_index:len(arr2)]
            break
        if array2_index == len(arr2):
            united_array += arr1[array1_index:len(arr1)]
            break
        if descending_order:
            if arr1[array1_index] >= arr2[array2_index]:
                united_array.append(arr1[array1_index])
                array1_index += 1
            else:
                united_array.append(arr2[array2_index])
                array2_index += 1
        else:
            if arr1[array1_index] <= arr2[array2_index]:
                united_array.append(arr1[array1_index])
                array1_index += 1
            else:
                united_array.append(arr2[array2_index])
                array2_index += 1
    return united_array


algoTester = AlgoTester()
algoTester.setTestArray([10, 29, 18, 2, 4, 91, 105, 0, 0, 101, -10])
algoTester.calculateTime(strand_sort, start_amount=1000, epochs=10)
algoTester.drawGraphics('Strand Sort Algorythm')