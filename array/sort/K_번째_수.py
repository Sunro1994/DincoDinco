# 1번쨰
#  0 :1  2   3  4:  5 6
# [1, 5, 2, 6, 3, 7, 4]
# [5,2,6,3]
# [2,3,5,6] -> 5

# [ 1, 5, 2, 6, 3 ,7 , 4]
# [ 1, 2, 3 , 4 5 6 7 ] -> 3

def solution(array, commands):
    answer = []

    for command in commands:
        limited_arr = array[command[0]-1:command[1]]
        limited_arr.sort()
        answer.append(limited_arr[command[2]-1])

    return answer

