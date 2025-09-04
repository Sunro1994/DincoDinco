import sys

n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())

# 양 끝에 탐색 시작 포인트를 둔다
start, end = 0, n-1
cnt = 0

while start < end:
    tmp = nums[start] + nums[end]
    # 배열은 정렬된 상태이므로 조건을 만족하면 수가 작은 쪽인 start부분의 포인트를 움직여준다.
    if tmp == x:
        cnt += 1
        start += 1

    elif tmp > x:
        end -= 1

    else:
        start += 1

print(cnt)


n = 9
nums = [1,2,3 ,5 ,7, 9, 10, 11, 12]

x = 13