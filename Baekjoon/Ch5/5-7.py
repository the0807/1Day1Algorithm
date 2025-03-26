# 2675번 "문자열 반복"

num = int(input())

for _ in range(num):
    r, s = input().split()

    for i in range(len(s)):
        print(s[i] * int(r), end = '')
    print('')
