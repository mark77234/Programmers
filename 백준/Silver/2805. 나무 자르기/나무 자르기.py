# 가져갈 나무의 수 N, 나무의 길이 M
# 나무의 높이들

N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)

answer = 0
while left <= right:
    mid = (left + right) // 2 # 중앙으로 나누기(중앙값)

    total = 0 # 들고갈 나무 길이
    for tree in trees:
        if tree > mid:
            total += tree - mid # 나무 자르기

    if total >= M: # 만약 들고갈 나무 길이가 M보다 크거나 같으면
        answer = mid # answer에 mid 넣어놓고
        left = mid + 1 # 왼쪽 탐색 -> 한칸 옮김
    else:
        right = mid - 1 # 아닌경우 우측 탐색 <- 한칸 옮김

print(answer)
