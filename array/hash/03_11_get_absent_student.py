# 1. 2중 반복문으로 모든 학생들을 조회하면서 존재 유무 파악
# 2. 정렬을 이용한 방법
# 3. 딕셔너리, 해시 테이블을 이용한 방법


def get_absent_stduent(all_array, present_array):
    dict = {}
    for student in all_array:
        dict[student] = True

    for present_array in present_array:
        del dict[present_array]

    for key in dict.keys():
        return key
    return None


