def solution(participant, completion):

    hash = {}
    for i in participant:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    for i in completion:
        if hash[i] > 1:
            hash[i] -= 1
        else:
            del hash[i]

    answer = list(hash.keys())[0]
    return answer