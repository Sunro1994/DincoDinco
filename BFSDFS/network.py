from collections import deque

def dfs(i, visited, computers):
    visited[i] = True
    n = len(computers)
    for neighbor in range(n):
        if computers[i][neighbor] == 1  and not visited[neighbor]:
            dfs(neighbor, visited, computers)

def bfs(i, visited, computers):
    queue = deque([i])
    visited[i] = True

    while queue:
        current_node = queue.popleft()

        n = len(computers)
        for neighbor in range(n):
            if computers[neighbor][current_node] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


def solution(n, computers):
    visited = [False] * n
    network_count = 0
    for i in range(n):
        if not visited[i]:
            network_count += 1
            bfs(i, visited, computers)
    return network_count



print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), "예상 결과값 : 2")