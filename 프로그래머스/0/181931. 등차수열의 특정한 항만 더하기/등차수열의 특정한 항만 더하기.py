def solution(a,d,included):
    sum = 0
    result = 0
    for i in range(len(included)):
        if i ==0:
            sum += a
        else:
            sum +=d
        if included[i]:
            result += sum
    return result