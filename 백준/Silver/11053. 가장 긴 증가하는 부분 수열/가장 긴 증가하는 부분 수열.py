N = int(input())
numbers = list(map(int, input().split()))

li = [1] * N

for i in range(N):  # 5
    for j in range(i):
        if numbers[j] < numbers[i]:  # 현재 인덱스 값이랑 나머지 인덱스 값들 비교
            li[i] = max(li[i], li[j] + 1)  # 둘 중 더 큰값에 +1
print(max(li))
