import sys
from bisect import bisect_left

def main():
    input = sys.stdin.readline

    N = int(input().strip())
    array = list(map(int, input().split()))

    uniq = sorted(set(array))

    answer = [bisect_left(uniq,x) for x in array]

    print(' '.join(map(str, answer)))

if __name__ == '__main__':
    main()