import heapq


def solution(scoville, K):
    heap = []
    cnt = 0

    for i in scoville:
        heapq.heappush(heap, i)

    while K > heap[0]:
        cnt += 1
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)

        if len(heap) == 1 and heap[0] < K:
            return -1

    return cnt