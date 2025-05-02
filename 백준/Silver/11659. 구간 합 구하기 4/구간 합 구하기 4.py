import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num = list(map(int, input().split()))
tot = [0]
tmp = 0

for i in num:
    tmp += i
    tot.append(tmp)

for i in range(M):
    i, j = map(int, input().split())
    print(tot[j] - tot[i - 1])
