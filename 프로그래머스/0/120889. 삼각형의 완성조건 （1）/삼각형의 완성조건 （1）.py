def solution(sides):
    max_num =  max(sides)
    sides.pop(sides.index(max_num))
    return 1 if max_num < sum(sides) else 2
