a, b = map(int, input().split())

answer = []
k = 1

while len(answer) < a:
    if str(b) not in str(k):
        answer.append(k)
    k += 1

print(max(answer))
