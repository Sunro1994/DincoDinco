def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):   # left부터 right까지 반복
        row = i // n                   # 몇 번째 행인지 계산
        col = i % n                    # 몇 번째 열인지 계산

        # 규칙: 값은 (row+1)과 (col+1) 중 더 큰 값
        if row >= col:
            answer.append(row + 1)
        else:
            answer.append(col + 1)

    return answer