from collections import deque
import sys

def main():
    input = sys.stdin.readline

    result = []

    total_cnt, destroy_pos = map(int , input().split())

    dq = deque(range(1, (total_cnt+1)))

    while  dq:
        dq.rotate(-(total_cnt-1))
        result.append(dq.popleft())

    print("<", ", ".join(map(str, result)) + ">")

if __name__ == '__main__':
    main()
