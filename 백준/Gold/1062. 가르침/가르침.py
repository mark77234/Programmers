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
    words.append(word[4:-4])


if K >= 5:
    answer = []
    for i in combinations(alp, K - 5):
        possible = set(i)
        possible |= set("antic")
        cnt = 0
        for word in words:
            read = True
            for j in word:
                if j not in possible:
                    read = False
                    break
            if read:
                cnt += 1
        answer.append(cnt)
    print(max(answer))
else:
    print(0)
