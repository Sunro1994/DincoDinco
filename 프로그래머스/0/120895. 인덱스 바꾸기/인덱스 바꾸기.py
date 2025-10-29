def solution(my_string, num1, num2):
    answer =0
    arr = [i for i in my_string]
    arr[num1], arr[num2] = arr[num2], arr[num1]
    return "".join(arr)