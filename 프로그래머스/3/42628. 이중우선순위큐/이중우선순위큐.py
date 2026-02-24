import heapq


def solution(operations):
    min_heap = []
    max_heap = []

    for operation in operations:
        operator, val = operation.split()

        if operator == "I":
            heapq.heappush(min_heap, int(val))
            heapq.heappush(max_heap, -int(val))
        elif operator == "D" and val == "-1":
            if min_heap:
                tmp = -heapq.heappop(min_heap)
                max_heap.remove(tmp)
                heapq.heapify(max_heap)
        else:
            if max_heap:
                tmp = -heapq.heappop(max_heap)
                min_heap.remove(tmp)
                heapq.heapify(min_heap)

    if min_heap:
        min_ans = heapq.heappop(min_heap)
        max_ans = -heapq.heappop(max_heap)
    else:
        min_ans = 0
        max_ans = 0
    return [max_ans, min_ans]
