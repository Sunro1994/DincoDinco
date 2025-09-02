import sys
import math

def main():
    input = sys.stdin.readline

    # 1. 입력값을 문자열로 받기
    room_number = input().strip()

    # 2. 0~9까지 숫자 카운트
    counts = [0] * 10
    for ch in room_number:
        counts[int(ch)] += 1

    # 3. 6과 9는 서로 뒤집어서 사용 가능
    combined = counts[6] + counts[9]
    counts[6] = math.ceil(combined / 2)  # 올림 처리
    counts[9] = 0  # 9는 더 이상 개별로 세지 않음

    print(max(counts))

if __name__ == "__main__":
    main()