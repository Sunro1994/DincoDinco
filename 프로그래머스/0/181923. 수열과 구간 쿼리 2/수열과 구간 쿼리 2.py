def solution(arr, queries):
    result = []
    for query in queries:
        temp = [arr[i] for i in range(query[0], query[1]+1) if arr[i] > query[2]]
        if temp:
            result.append(min(temp))
        else:
            result.append(-1)

    return result
