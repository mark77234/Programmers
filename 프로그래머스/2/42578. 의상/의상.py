def solution(clothes):
    hash = {}
    tot = 1

    for part in clothes:
        if part[1] not in hash:
            hash[part[1]] = [part[0]]  # 리스트로 초기화
        else:
            hash[part[1]].append(part[0])

    for key in hash:
        tot *= len(hash[key]) + 1

    return tot - 1