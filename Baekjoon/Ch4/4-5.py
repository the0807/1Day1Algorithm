# 10810번 "공 넣기"

import sys

n, m = map(int, sys.stdin.readline().split())

basket = [0] * n

for a in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for num in range(i - 1, j):
        basket[num] = k

for i in basket:
    print(i, end=' ')