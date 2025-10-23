def solution(box, n):
    answer = 1
    for len in box:
        answer *= len//n

    return answer