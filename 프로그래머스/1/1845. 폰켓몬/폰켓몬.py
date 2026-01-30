def solution(nums):
    hash = {}

    for i in nums:
        if i not in hash:
            hash[i] = "포켓몬"

    variety = len(list(hash.keys()))
    max_selection = len(nums) // 2

    if variety > max_selection:
        answer = max_selection
    else:
        answer = variety

    return answer
