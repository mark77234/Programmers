def solution(s):
    li = s.split()
    answer = []
    for i in li:
        answer.append(int(i))

    top = max(answer)
    low = min(answer)

    tmp = str(low) + " " + str(top)
    return tmp