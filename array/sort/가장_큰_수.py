# 1. functools를 import
import functools
# 2. 정렬 custom 함수를 생성
def sort(x,y):
    xy = x+y
    yx = y+x

    if yx > xy:
        return 1
    elif yx < xy:
        return -1
    else:
        return 0


# 3. 숫자를 문자열로 변환한 배열을 생성
def solution(numbers):
    str_arr = [str(x) for x in numbers]
# 4. custom한 내용으로 정렬
    str_arr.sort(key = functools.cmp_to_key(sort))
# 5. ""으로 join
    answer= "".join(str_arr)
# 6. 반환
    return str(int(answer))



print(solution([6, 10, 2]	))