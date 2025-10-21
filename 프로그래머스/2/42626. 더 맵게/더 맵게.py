import heapq

def solution(scoville,K):
    heap = []
    cnt =0
    for item in scoville:
        heapq.heappush(heap, item)
    min_num = min(scoville)
    while heap and heap[0] < K:
        if len(heap) == 1:
            return -1
        min1  = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        heapq.heappush(heap, min1 + min2*2)
        cnt +=1
    return cnt