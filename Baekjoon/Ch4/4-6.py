# 10813번 "공 바꾸기"

import sys

n, m = map(int, sys.stdin.readline().split())
box = [i for i in range(1, n+1)]

for a in range(m):
    i, j = map(int, sys.stdin.readline().split())
    temp = box[i-1]
    box[i-1]=box[j-1]
    box[j-1]=temp

for b in box:
    print(b, end=' ')