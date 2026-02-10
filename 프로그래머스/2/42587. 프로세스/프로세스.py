from collections import deque


def solution(priorities, location):
    answer = []

    q = deque((priorities[i], i) for i in range(len(priorities)))

    while q:
        tmp = q.popleft()

        if any(tmp[0] < i[0] for i in q):
            q.append(tmp)

        else:
            answer.append(tmp[1])

    return answer.index(location) + 1