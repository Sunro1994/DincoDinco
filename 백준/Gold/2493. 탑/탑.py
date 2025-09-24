import sys

input = sys.stdin.readline


def main():
    n = int(input())
    heights = list(map(int, input().split()))
    stack = []       # (index, height)
    answer = []

    for i in range(n):
        while stack and stack[-1][1] <= heights[i]:
            stack.pop()
        if stack:
            answer.append(stack[-1][0] + 1)   # 1-based
        else:
            answer.append(0)
        stack.append((i, heights[i]))

    print(' '.join(map(str, answer)))


if __name__ == '__main__':
    main()