example = [0, 3, 5, 6, 1, 2, 4]

def find_random_number(target, arrays):
    left = 0
    right = len(arrays) -1
    mid = (left+right)//2

    arrays.sort()

    while left <= right:
        if arrays[mid] == target:
            return True
        elif arrays[mid] < target:
            left = mid +1
        else:
            right = mid -1
        mid = (left + right)//2

    return False

print(find_random_number(2, example))