def BubbleSort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swapped = True
        if not swapped:
            break


array = [-1, 29, 0, 1125, -3]

BubbleSort(array)
print("Sorted Array in Ascending Order:")
print(array)
