from collections import deque


def solution(s):
    q = deque(s)
    li = []

    while q:
        tmp = q.popleft()

        if tmp == "(":
            li.append(tmp)
        else:
            if "(" in li:
                li.pop()
            else:
                return False

    if li:
        return False

    return True