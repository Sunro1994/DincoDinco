array = [ 4, 6, 2, 9, 1]

def selection_sort(array):
    n = len(array)

    for i in range(n-1):
        min_index  = i
        for j in range(n-i):
            print(i, j)
            if array[i+j] < array[min_index]:
                min_index = i+j


        array[i], array[min_index] = array[min_index], array[i]
    return array
print(selection_sort(array))