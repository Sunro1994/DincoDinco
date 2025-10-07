from collections import deque


def solution(priorities, location):
    answer = 0
    # (중요도, 원래 위치)를 담는 큐를 생성
    queue = deque([(p, i) for i, p in enumerate(priorities)])

    while queue:
        # 1. 큐의 가장 앞에서 문서를 꺼낸다.
        current_doc = queue.popleft()
        current_priority = current_doc[0]
        current_location = current_doc[1]

        # 2. 큐에 남아있는 문서 중 우선순위가 더 높은 것이 있는지 확인
        # any()는 하나라도 True가 있으면 True를 반환하는 효율적인 함수
        if any(current_priority < other_doc[0] for other_doc in queue):
            # 3. 있다면, 꺼낸 문서를 큐의 맨 뒤에 다시 넣는다.
            queue.append(current_doc)
        else:
            # 4. 없다면, 이 문서를 인쇄한다.
            answer += 1  # 인쇄 순서 증가

            # 5. 방금 인쇄한 문서가 내가 찾던 문서인지 확인
            if current_location == location:
                return answer  # 맞다면 현재 인쇄 순서를 반환하고 종료


# 테스트
print(solution([1, 1, 9, 1, 1, 1], 0))  # 출력: 5
print(solution([2, 1, 3, 2], 2))  # 출력: 1