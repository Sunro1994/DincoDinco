from collections import deque


def solution(prices):
    queue = deque(prices)
    result = []
    while queue:
        i = queue.popleft()
        price_not_fall_period = 0
        for next_price in queue:
            if i <= next_price:
                price_not_fall_period += 1
            else:
                price_not_fall_period += 1
                break
        result.append(price_not_fall_period)
    return result