def solution(genres, plays):
    hash = {}
    total = {}

    for i in range(len(genres)):

        if genres[i] in hash:
            total[genres[i]] += plays[i]
            hash[genres[i]].append((plays[i], i))
        else:
            total[genres[i]] = plays[i]
            hash[genres[i]] = [(plays[i], i)]

    for i in hash:
        hash[i].sort(key=lambda x: (-x[0], x[1]))

    genre_rank = sorted(total.keys(), key=lambda x: total[x], reverse=True)

    print(hash)
    print(total)
    print(genre_rank)
    answer = []

    for genre in genre_rank:
        for views, i in hash[genre][:2]:
            answer.append(i)

    return answer
