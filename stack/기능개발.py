def solution(progresses, speeds):
    answer = []
    rest_progress_rate = []
    for i in range(len(progresses)):
        rest_progress_rate.append(100 - progresses[i])

    rest_day = []
    for i in range(len(speeds)):
        share = rest_progress_rate[i] // speeds[i]
        remainder = rest_progress_rate[i] % speeds[i]
        if remainder > 0:
            share += 1
        rest_day.append(share)

    if not rest_day:
        return []

    cnt = 0
    max_day = rest_day[0] # 첫 번째 작업을 배포 기준일로 설정

    for day in rest_day:
        if day <= max_day: # 기준일보다 빨리 끝나면 같은 배포 그룹에 포함
            cnt += 1
        else: # 기준일보다 오래 걸리면
            answer.append(cnt) # 이전까지의 그룹을 배포
            cnt = 1 # 새로운 그룹 시작
            max_day = day # 기준일을 새로 설정

    answer.append(cnt) # 마지막 그룹을 answer에 추가

    return answer

# 테스트
print(f"결과: {solution([93, 30, 55], [1, 30, 5])}") # 예상 결과: [2, 1]
# rest_day: [7, 3, 9]

print(f"결과: {solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])}") # 예상 결과: [1, 3, 2]
# rest_day: [5, 10, 1, 1, 20, 1]