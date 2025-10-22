def solution(n, lost, reserve):

    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for l in sorted(list(set_lost)):
        if l-1 in set_reserve:
            set_reserve.remove(l-1)
        elif l+1 in set_reserve:
            set_reserve.remove(l+1)
        else:
            n -=1

    return n