def dfs(i, visited, computers):
    visited[i] = True
    n = len(computers)
    for neighbor in range(n):
        if computers[i][neighbor] == 1  and not visited[neighbor]:
            dfs(neighbor, visited, computers)


def solution(n, computers):
    visited = [False] * n
    network_count = 0
    for i in range(n):
        if not visited[i]:
            network_count += 1
            dfs(i, visited, computers)
    return network_count
