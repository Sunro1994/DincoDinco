def solution(n, times):
    answer = 0
    left = 1
    right = n * max(times)

    while left <= right:
        mid = (left + right) // 2
        total_people = sum([mid // time for time in times])

        if total_people >= n:
            answer = mid
            right = mid -1
        else:
            left = mid + 1
    return answer