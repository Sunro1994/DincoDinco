A = int(input())
B = int(input())
C = int(input())

result = A * B * C
counts = [0] * 10  # 0~9까지 카운트

# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



for num in str(result):
    counts[int(num)] += 1

 # reslut가 17037300이라면, conuts[1] =1, conuts[7] = 3, conuts[0] = 4
 # counts[3] = 1, counts[7] = 1, counts[3] = 2, counts[0] = 2, counts[0] = 3

for count in counts:
    print(count)
# 0 ~9까지 출력
# [3, 1, 0, 2, 0, 0, 0, 2, 0, 0]


def math(a, b, c):
    freq = {}
    res = a * b * c

    for num in str(res):
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # 0부터 9까지 차례대로 출력
    for i in range(10):
        print(freq.get(str(i), 0))

# 예시 실행
math(150, 266, 427)