room_number = input()  # 방 번호 입력

# 숫자 개수 세기
count = [0] * 10
for num in room_number:
    count[int(num)] += 1

# 6과 9 합쳐서 처리
six_nine = count[6] + count[9]
# 올림 처리: (합 + 1) // 2
count[6] = (six_nine + 1) // 2
count[9] = 0

# 최소 세트 수 = 가장 많이 필요한 숫자
print(max(count))