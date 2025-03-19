# 10871번 "X보다 작은 수"

import sys

n, x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if a[i] < x:
        print(a[i], end=" ")