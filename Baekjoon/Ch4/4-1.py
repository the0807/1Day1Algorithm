# 10807번 "개수 세기"

import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(n_list.count(v))