def solution(distance, rocks, n):
    # 1. 바위 위치를 정렬하고 시작(0)과 도착(distance) 지점을 추가합니다.
    rocks.sort()
    all_position = [0] + rocks + [distance]


    # 2. 이분 탐색을 위한 범위를 설정합니다.
    # start는 가능한 최소 거리, end는 가능한 최대 거리입니다.
    start = 1
    end = distance


    # 3. 이분 탐색을 시작합니다.
    while start < end:
        # mid는 우리가 확인해볼 '최소 거리'의 후보입니다.
        mid = (start+ end) //2

        # 4. 'mid'를 최소 거리로 만들기 위해 몇 개의 바위를 제거해야 하는지 계산합니다.
        # last_position은 마지막으로 남겨둔 바위의 위치입니다. 처음엔 시작점(0)입니다
        last_position = 0
        remove_rock = 0

        # 0(시작점)을 제외한 첫 번째 바위부터 순회합니다.
        for i in range(1,len(all_position)):
            # 현재 바위와 마지막으로 남겨둔 바위 사이의 거리를 계산합니다.
            diff = all_position[i] - last_position
            # 거리가 우리가 정한 최소 거리(mid)보다 짧다면,
            if diff < mid:
            # 현재 바위(all_points[i])를 제거해야 합니다.
                remove_rock += 1
            # 거리가 mid 이상이라면, 이 바위는 제거할 필요가 없습니다.
            else:
            # 이 바위를 새로운 기준점으로 삼습니다.
                last_position = all_position[i]

        # 5. 제거한 바위의 수를 n과 비교하여 탐색 범위를 조정합니다.
            # 너무 많은 바위를 제거했다면, mid 값이 너무 큰 것입니다.
        if remove_rock > n:
            # 최소 거리의 기준을 낮춰야 합니다.
            end = mid -1
            # n개 이하의 바위를 제거해서 성공했다면, mid는 가능한 값입니다.
        else:
            # 현재 mid를 정답 후보로 저장하고, 더 큰 최소 거리가 가능한지 탐색합니다.
            answer = mid
            start = mid + 1

    return answer

# --- 예시 테스트 ---
distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(f"결과: {solution(distance, rocks, n)}")  # 예상 결과: 4