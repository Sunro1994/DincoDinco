import sys
from collections import deque


def main():
    input = sys.stdin.readline

    count = int(input())

    for i in range(count):
        command = input().rstrip()
        left = deque()
        right = deque()

        for c in command:
            if c == '<': #pb
                if left:
                    right.appendleft(left.pop())
            elif c == '>': #pb
                if right:
                    left.append(right.popleft())
            elif c == '-':
                if left:
                    left.pop()
            else:
                left.append(c)

        print("".join(left) + "".join(right))


if __name__ == '__main__':
    main()