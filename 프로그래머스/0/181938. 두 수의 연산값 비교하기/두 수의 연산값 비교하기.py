def solution(a, b):

    if int(str(a)+str(b)) > 2 * a * b:
        return int(str(a) + str(b))
    else:
        return 2 * a * b