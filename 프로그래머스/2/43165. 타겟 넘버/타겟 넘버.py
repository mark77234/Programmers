def solution(numbers, target):
    answer = 0
    bfs = [0]
    for i in numbers:
        tmp = []

        for j in bfs:
            tmp.append(j + i)
            tmp.append(j - i)

        bfs = tmp

    for num in bfs:
        if num == target:
            answer += 1
    return answer