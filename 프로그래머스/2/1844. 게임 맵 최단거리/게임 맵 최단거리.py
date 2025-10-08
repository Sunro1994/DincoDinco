from collections import deque

#1 .방향 벡터
dr = [0, 0, 1, -1]  # 열
dc = [1, -1, 0, 0]  # 행
def solution(maps):
    n,m = len(maps), len(maps[0])
    #2. 큐 초기화, 시작지점 설정
    queue = deque([(0,0,1)])
    #3. 방문처리
    maps[0][0] = 0
    #4. BFS 시작
    while queue:
        r,c,d = queue.popleft()
        #5. 도달 여부 파악
        if r == n -1 and c == m-1:
            return d
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<m and maps[nr][nc] == 1:
                maps[nr][nc] = 0
                queue.append((nr,nc,d+1))

    return -1
