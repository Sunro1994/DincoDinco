import sys
from collections import deque


def main():
    input = sys.stdin.readline

    text = input().strip() #문자 (strip으로 개행 문자 제거)
    order_count = int(input()) #명령 횟수

    #커서 기준으로 왼쪽 오른쪽이 갈림
    left = deque(text)
    right = deque()
    # 나머지 명령어 입력받아서 switch-case처리?

    for _ in range(order_count):
        command = input().split()
        command1 = command[0]

#abcd
        if command1 == 'L': ## abc|d (abc) (d)
            if left:
                right.appendleft(left.pop())
        elif command1 == 'D': ## abcd (abcd)
            if right:
                left.append(right.popleft())
        elif command1 == 'B':
            if left:
                left.pop() ## abc |   커서기준 왼쪽 제거
        elif command1 == 'P':
            left.append(command[1]) ## abcd 커서기준 왼쪽에 추가하게 됨

    print("".join(left) + "".join(right))


if __name__ == '__main__':
    main()

