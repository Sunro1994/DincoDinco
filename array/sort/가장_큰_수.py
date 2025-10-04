import functools

def compare(x,y):
    xy = x+y
    yx = y+x

    # yx가 더 크면 1
    if yx> xy:
        return 1
    # 반대가 더 크면 -1
    elif yx< xy:
        return -1
    # 같으면 0
    else:
        return 0


def solution(numbers):
    str_numbers = [str(x) for x in numbers]

    str_numbers.sort(key = functools.cmp_to_key(compare))

    answer = "".join(str_numbers)

    answer = str(int(answer))


    return answer


