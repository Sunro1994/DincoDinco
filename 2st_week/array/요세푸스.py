import sys
from collections import deque    

input = sys.stdin.readline
N, K = map(int, input().split())
q = deque(range(1, N + 1))
result = []

while q:         
    for _ in range(K - 1):
        q.append(q.popleft())
        
    result.append(q.popleft())

print("<" + ", ".join(map(str, result)) + ">")




# 1 2 3 4 5 6 7   
# 3 4 5 6 7 1 2   - 3
# 4 5 6 7 1 2  
# 6 7 1 2 4 5    - 6
# 7 1 2 4 5
# 2 4 5 7 1    -   2
# 4 5 7 1 
# 7 1 4 5     -  7      


# <3, 6, 2, 7, 5, 1, 4>

 