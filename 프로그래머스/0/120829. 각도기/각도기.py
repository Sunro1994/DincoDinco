def solution(angle):
    if angle <= 90:
        return 1 if angle<90 else 2
    elif angle <=180:
        return 3 if angle<180 else 4