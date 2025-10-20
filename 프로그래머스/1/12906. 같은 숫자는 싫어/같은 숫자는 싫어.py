# 요구사항
# 배열 arr에서 연속으로 나타나는 숫자는 하나만 남기고 전부 제거
# 제거된 후 남은 수들을 반환할때는 배열arr의 원소의 순서를 유지해야 한다.
def solution(arr):
    answer= []
    for i in range(len(arr)):
        if i == len(arr)-1:
            answer.append(arr[i])
        elif arr[i] != arr[i+1]:
            answer.append(arr[i])
    return answer