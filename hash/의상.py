from collections import defaultdict


def solution(clothes):
    # 키가 없을 경우 자동으로 빈 리스트([])를 생성하는 딕셔너리를 만듭니다.
    closet = defaultdict(list)

    for name, kind in clothes:
        # if/else로 키 존재 여부를 체크할 필요 없이 그냥 바로 append하면 됩니다.
        # 'headgear'가 처음 나오면 자동으로 closet['headgear'] = [] 가 먼저 실행된 후 append 됩니다.
        closet[kind].append(name)

    print(closet)
    # 출력: defaultdict(<class 'list'>, {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']})

    # (이후 조합 계산 로직 추가...)

    return 0


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])