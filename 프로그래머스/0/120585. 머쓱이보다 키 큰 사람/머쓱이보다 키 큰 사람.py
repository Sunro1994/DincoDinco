def solution(array, height):
    return sum([1 for i in range(len(array)) if array[i] > height])