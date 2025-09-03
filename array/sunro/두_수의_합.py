import sys

def Main():
    input = sys.stdin.readline
    n = int(input().strip())
    A = list(map(int, input().split()))
    x = int(input().strip())

    A.sort()

    count = 0
    left, right = 0, n - 1

    while left < right:
        current_sum = A[left] + A[right]
        if current_sum == x:
            count += 1
            left += 1
        elif current_sum < x:
            left += 1
        else:
            right -= 1

    print(count)

if __name__ == "__main__":
    Main()
