from collections import deque

def solution(prices):
    queue = deque(prices)
    answer =[]

    while queue:
        target = queue.popleft()
        not_failed_price = 0
        for price in queue:
            if target <= price:
                not_failed_price += 1
            else:
                not_failed_price +=1
                break
        answer.append(not_failed_price)
    print(answer)


solution([1, 2, 3, 2, 3])