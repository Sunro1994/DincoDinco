def solution(phone_book):
    # 1. 모든 전화번호를 해시맵(딕셔너리)에 저장합니다.
    #    조회(in) 연산의 시간 복잡도를 평균 O(1)로 만들기 위함입니다.
    hash_map = {number: 1 for number in phone_book}
    print(hash_map)

    # 2. 전화번호부를 다시 순회합니다.
    for phone_number in phone_book:
        # 3. 각 전화번호에 대해, 접두어가 될 수 있는 부분 문자열을 만듭니다.
        prefix = ""
        for digit in phone_number:
            prefix += digit

            # 4. 만들어진 접두어가 해시맵에 존재하는지 확인합니다.
            #    단, 자기 자신과 똑같은 경우는 접두어가 아니므로 제외합니다.
            #    (예: phone_book에 "123"만 있을 때, "123"의 접두어 "123"을 찾는 경우)
            if prefix in hash_map and prefix != phone_number:
                # 접두어를 찾았으므로 즉시 False를 반환합니다.
                return False

    # 모든 번호를 확인했는데도 접두어 관계를 찾지 못했다면 True를 반환합니다.
    return True


# --- 테스트 ---
phone_book_1 = ["119", "97674223", "1195524421"]
print(f"결과 1: {solution(phone_book_1)}")  # False

phone_book_2 = ["123", "456", "789"]
print(f"결과 2: {solution(phone_book_2)}")  # True

phone_book_3 = ["12", "123", "1235", "567", "88"]
print(f"결과 3: {solution(phone_book_3)}")  # False