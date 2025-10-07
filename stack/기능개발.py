def solution(progresses, speeds):
    answer = []
    rest_progress = []
    #1. rest_progress= progress의 100 - 각 값
    for progress in progresses:
        rest_progress.append(100-progress)
    #2. share = speeds로 나눈 값 (나머지가 있는경우 +1)
    rest_day = []
    print("rest_progress : " , rest_progress)
    for i in range(len(rest_progress)):
        devide = rest_progress[i] // speeds[i]
        share = rest_progress[i] % speeds[i]
        if share >0:
            devide = devide + 1
        rest_day.append(devide)
    print("rest_day : " , rest_day)

    #3. rest_day를 순회(0번째 인덱스를 기준으로 1부터 시작)
    max_day = rest_day[0]
    cnt = 1
    for i in range(1, len(rest_day)):
        print(i)
    #4.첫 값을 max값으로 잡고 순회하며 그 값보다 작으면 +1
        if max_day >= rest_day[i]:
            cnt +=1
    #5. 그 값보다 크면 answer에 값을 넣고 max값을 업데이트
        else:
            answer.append(cnt)
            max_day = rest_day[i]
            cnt = 1
    answer.append(cnt)
    return answer

# 테스트
print(f"결과: {solution([93, 30, 55], [1, 30, 5])}") # 예상 결과: [2, 1]
# rest_day: [7, 3, 9]

print(f"결과: {solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])}") # 예상 결과: [1, 3, 2]
# rest_day: [5, 10, 1, 1, 20, 1]