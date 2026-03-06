# anta ... tica -> a,n,t,i,c

# r
# helo
# r
from itertools import combinations
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

alp = "bdefghjklmopqrsuvwxyz"
words = []


for i in range(N):
    word = input()
    words.append(set(word[4:-4]))


if K >= 5:
    answer = 0
    for i in combinations(alp, K - 5):
        possible = set(i)
        possible |= set("antic")
        cnt = 0
        for word in words:
            if word <= possible:
                cnt += 1

        answer = max(answer, cnt)
    print(answer)
else:
    print(0)
