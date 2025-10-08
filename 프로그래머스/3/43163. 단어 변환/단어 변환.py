from collections import deque


def solution(begin, target, words):
    # 1. 사전 확인
    if target not in words:
        return 0

    # 2. BFS 초기화
    queue = deque([(begin, 0)])  # (단어, 변환 횟수)
    visited = {begin}

    # 3. BFS 루프
    while queue:
        current_word, count = queue.popleft()

        # 목표 확인
        if current_word == target:
            return count

        # 다음 단계 탐색
        for next_word in words:
            if next_word not in visited and is_convertible(current_word, next_word):
                visited.add(next_word)
                queue.append((next_word, count + 1))

    # 4. 탐색 실패
    return 0


def is_convertible(word1, word2):
    diff_count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1

    return diff_count == 1
