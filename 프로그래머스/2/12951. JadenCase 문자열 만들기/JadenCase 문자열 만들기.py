def solution(s):
    li = s.split(" ")

    for i in range(len(li)):
        li[i] = li[i].capitalize()
    answer = " ".join(li)
    return answer


