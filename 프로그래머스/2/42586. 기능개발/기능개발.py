
def solution(progresses, speeds):
    day = []
    items = len(progresses)
    answer = []

    for i in range(items):
        if (100 - progresses[i]) % speeds[i] == 0:  # 딱 안나뉘어 떨어지면 +1일
            day.append((100 - progresses[i]) // speeds[i])
        else:
            day.append((100 - progresses[i]) // speeds[i] + 1)

    print(day)

    for i in range(len(day)):
        tmp = 1
        for j in range(i + 1, len(day) + 1):
            print(i)
            if day[i] == "X":
                continue
            if j == len(day):
                answer.append(tmp)
                break
            if day[i] < day[j]:
                answer.append(tmp)
                break
            else:
                day[j] = "X"
                tmp += 1

            print(day)
    return answer
