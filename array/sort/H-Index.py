# 1. 정렬
# 2. 이분탐색을 하기 위한 시작, 마지막, 중간지점 설정
# 3. while문을 탐색하면서 맞는 조건 도출
# 4. 중간값보다 결과가 작을 경우 왼쪽, 중간값보다 결과가 클경우 정답
from logging import critical


def solution(citations):
    answer = 0
    citations.sort()

    left = 0
    right = len(citations)
    while left <= right:
        mid = (left + right) // 2
        cnt =0
        for citation in citations:
            if citation >= mid:
                cnt +=1

        # "h번 이상 인용된 논문이 h편 이상" 이라는 조건을 만족하는가?
        if cnt >= mid:
            answer = mid
            left = mid +1
        else:
            right = mid - 1
    return answer

print(solution([0,3,4,5,5,5,6]	))