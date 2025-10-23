def solution(my_string):
    arr = [int(string) for string in my_string if string.isdigit()]
    arr.sort()
    return arr