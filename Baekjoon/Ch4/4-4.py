# 2562번 "최댓값"

import sys

list_n = []
for i in range(9):
    n = int(sys.stdin.readline())

    list_n.append(n)

print(max(list_n), list_n.index(max(list_n))+1)