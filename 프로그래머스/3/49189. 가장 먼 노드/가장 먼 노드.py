from collections import deque


def solution(n, vertex):
    answer = 0
    # 방문 인접 리스트 생성
    vertexList = [[] for _ in range(n+1)]

    for v in vertex:
        vertexList[v[0]].append(v[1])
        vertexList[v[1]].append(v[0])
    dist = [-1 for _ in range(n+1)]

    queue = deque([1])
    dist[1] = 0

    while queue:
        v = queue.popleft()
        for w in vertexList[v]:
            if dist[w] == -1:
                dist[w] = dist[v] + 1
                queue.append(w)

    max_dist = max(dist)
    for d in dist:
        if d == max_dist:
            answer += 1

    return answer



print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))