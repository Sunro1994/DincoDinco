import sys
input = sys.stdin.readline

def classify(s: str) -> int:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            # 불일치 시 왼쪽 or 오른쪽 하나를 건너뛰어 검사
            if is_pal_range(s, l+1, r) or is_pal_range(s, l, r-1):
                return 1
            else:
                return 2
    return 0

def is_pal_range(s: str, i: int, j: int) -> bool:
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()  # 개행 제거 중요
        print(classify(s))

if __name__ == "__main__":
    main()