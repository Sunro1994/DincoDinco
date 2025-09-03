def solution(n, left, right):
    """
    n: 배열의 크기 (n x n)
    left, right: 평탄화된 1차원 배열에서 반환할 시작, 끝 인덱스 (inclusive)
    """
    answer = []

    # left부터 right까지 하나씩 인덱스를 계산
    for idx in range(left, right + 1):
        row = idx // n  # 해당 인덱스의 행
        col = idx % n  # 해당 인덱스의 열
        value = max(row, col) + 1  # 규칙에 따른 값 계산
        answer.append(value)

    return answer