import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline

    N = int(input().strip())
    N_number = list(map(int, input().split()))
    N_number.sort()

    M = int(input().strip())
    M_number = list(map(int, input().split()))

    ans = []

    for q in M_number:
        ans.append('1' if bisect_inspection(N_number, q) else '0')

    print(' '.join(ans))

def bisect_inspection(arr, x):
    i = bisect_left(arr, x)
    return i < len(arr) and arr[i] == x

if __name__ == '__main__':
    main()