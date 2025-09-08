from collections import deque
import sys

def main():
    input = sys.stdin.readline

    num_range, destroy_pos = map(int, input().split())  # 한 줄에서 두 개 받는 방법

    dq = deque(range(1, num_range + 1))
    result = []

    while dq:
        dq.rotate(-(destroy_pos - 1))
        result.append(dq.popleft())

    return result

if __name__ == '__main__':
    main()
