import sys

def main():
    input = sys.stdin.readline

    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())

    product_str = str(a*b*c)

    counts = [0] * 10

    for char in product_str:
        counts[int(char)] += 1

    for cnt in counts:
        print(cnt)

if __name__ == '__main__':
    main()