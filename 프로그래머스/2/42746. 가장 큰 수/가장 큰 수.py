def solution(numbers):
    li = []
    answer = ""
    for number in numbers:
        li.append(str(number))

    li.sort(key=lambda x: x * 3, reverse=True)  # 1000자 이하

    for i in li:
        answer += i
    if li[0] == "0":
        return "0"
    return answer
