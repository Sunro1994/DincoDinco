import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    wheel = deque(['?'] * N)
    used = set()

    for _ in range(K):
        S, ch = input().split()
        S = int(S)

        wheel.rotate(S)

        if wheel[0] == '?':
            if ch in used:
                print("!")
                return
            wheel[0] = ch
            used.add(ch)
        elif wheel[0] != ch:
            print("!")
            return

    # 최종 출력: 화살표(=wheel[0])부터 시계방향으로 읽으면 됨
    print("".join(wheel))

if __name__ == "__main__":
    main()