def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()

    # H-Index가 될 수 있는 h값을 이분탐색으로 찾는다.
    # h의 범위는 0부터 논문 개수 n까지 가능하다.
    left = 0
    right = n

    while left <= right:
        # mid는 h-index의 후보 h
        mid = (left + right) // 2

        # 'mid'번 이상 인용된 논문이 몇 편인지 센다.
        count = 0
        for citation in citations:
            if citation >= mid:
                count += 1
        
        # "h번 이상 인용된 논문이 h편 이상" 이라는 조건을 만족하는가?
        if count >= mid:
            # 조건을 만족했으므로, mid는 H-Index 후보이다.
            # 더 큰 H-Index가 있을 수 있으므로 탐색 범위를 오른쪽으로 옮긴다.
            answer = mid  # 현재까지의 최적해를 저장
            left = mid + 1
        else:
            # 조건을 만족하지 못했으므로, mid는 H-Index가 될 수 없다.
            # h값을 줄여서 다시 탐색해야 하므로 탐색 범위를 왼쪽으로 옮긴다.
            right = mid - 1
            
    return answer

