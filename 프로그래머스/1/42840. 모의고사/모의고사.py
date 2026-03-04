student_1 = [1, 2, 3, 4, 5]
student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


def solution(answers):
    student = [0, 0, 0]
    answer = []

    for i in range(len(answers)):
        if student_1[i % len(student_1)] == answers[i]:
            student[0] += 1
        if student_2[i % len(student_2)] == answers[i]:
            student[1] += 1
        if student_3[i % len(student_3)] == answers[i]:
            student[2] += 1

    student_max = max(student)
    for i in range(len(student)):
        if student[i] == student_max:
            answer.append(i + 1)
    return answer